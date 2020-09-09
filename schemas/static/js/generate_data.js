        function generate_data()
        {
            
            if ($("#rows_number").val() > 0)
            {
                $("#rows_number").attr("style","border-color: none;");
                var today = new Date();
                var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();

                $.ajax({
                        type: 'POST',
                        async: true,
                        url: "/schema/ajax/generate_data/" + pk + "/" + $("#rows_number").val(),
                        headers: { "X-CSRFToken": csrf },
                        success: function(data) {
                            if (data['response'] == "Success") 
                            {
                                file_id = data['file_id'];
                                document.getElementById('data').innerHTML+='<tr>' + 
                                '<td>' + date + '</td>' + 
                                '<td id="processing_' + file_id + '"><div class="loader pull-right"></div><span style="color: rgb(115, 115, 117);">processing...</span></td>' + 
                                '<td><a id="' + file_id + '" class="not_ready" style="text-decoration: none; color: grey; cursor: default;">Download</a></td></tr>'
                                setInterval(wait_for_file_ready, 2000, file_id)
                            }
                        },
                        dataType: 'json',
                    });
            }
            else 
            {
                $("#rows_number").attr("style","border-color: red;");
            }
        }

        function wait_for_file_ready(file_id)
        {
            if (!file_ready(file_id))
            {
                $.ajax({
                        type: 'GET',
                        async: true,
                        url: "/schema/ajax/check_celery_job/" + file_id + "/",
                        success: function(data) {
                            if (data['response'] == "File ready") 
                            {
                                $("#" + file_id).attr("style","text-decoration: none; color: green; cursor: pointer;");
                                $("#" + file_id).attr("href","/schema/media/"+ file_id);
                                $("#" + file_id).attr("class","ready");
                                document.getElementById('processing_' + file_id).innerHTML='<span style="color: yellow;">Ready</span>'
                            }
                        },
                        dataType: 'json',
                    });
            }
        }

        function file_ready(file_id)
        {
            return $('#' + file_id).attr('class') == "ready";
        }