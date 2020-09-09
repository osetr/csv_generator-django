column_pk = 0;

function show_range()
{
    if ($( "#type" ).val() == "Text") $("#range").attr("style","padding-left:0px; display: block");
    else $("#range").attr("style","display: none")
}

function add_column()
{
    if ($("#name").val() && $("#order").val())
    {
        Type = $( "#type" ).val()
        if ($( "#type" ).val() == "Text") Type += '(' + Math.abs($( "#amount" ).val()) + ')'
        document.getElementById('columns').innerHTML+='<tr id="column' + column_pk + '"><td>' + $( "#name" ).val() + 
        '</td><td>' + Type + '</td><td>' + $( "#order" ).val() + 
        '</td><td><a onclick="del_column(' + column_pk + ')" style="color: red; cursor: pointer;">delete</a></td></tr>';
        $("#error").attr("style","padding-left: 10px; display: none")
        clean_form();
        
        column_pk ++;
    } else
    {
        $("#error").attr("style","padding-left: 10px; display: block")
    }
}

function del_column(pk)
{
    document.getElementById('column' + pk).innerHTML = ""
}

function clean_form()
{
    document.getElementById('column_form').reset();
    $("#range").attr("style","display: none")
}

$("#scheme_form").submit(function(e)
{
    $("#id_columns").attr("value",document.getElementById('columns').innerHTML)
    // e.preventDefault();
});