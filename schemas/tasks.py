from celery.task import periodic_task
from datetime import timedelta
from schemas.models import Processing
import os



@periodic_task(run_every=timedelta(seconds=1),
               name='reset_votes')
def build_csv_file():
    try:
        Processing.objects.first().delete()
    except AttributeError:
        print("There are no any work")
    else:
        print("Celery's just worked")

# celery worker -A project.celery -B