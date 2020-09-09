from celery.task import periodic_task
from datetime import timedelta
from schemas.models import Processing, Schema
import csv
from faker import Faker


Faker.seed(0)
fake = Faker()


def genPhone():
    return fake.phone_number()


def genText(number):
    return "".join([fake.sentence() for _ in range(int(number))])


def genFullName():
    return fake.name()


def genJob():
    return fake.job()


def genDate():
    return fake.date()


def genData(type, **kwargs):
    if type == "Full name":
        return genFullName()
    elif type == "Job":
        return genJob()
    elif type == "Phone number":
        return genPhone()
    elif type == "Text":
        return genText(kwargs["sentences_amount"])
    else:
        return genDate()


@periodic_task(run_every=timedelta(seconds=1), name="generate_file")
def build_csv_file():
    try:

        process = Processing.objects.filter(file_ready=False).first()
        file_id = process.file_id
        schema_id = process.schema_id
        rows = process.rows

        schema = Schema.objects.get(id=schema_id)
        separator = schema.separator
        columns = schema.columns

        names = [column["name"] for column in columns]
        types = [column["type"] for column in columns]
        additional_parameters = [
            column["additional_parameters"]
            for column in columns
        ]

        delimiter = {
            separator == "comma": ",",
            separator == "whitespace": " ",
            separator == "semicolon": ";",
        }[True]

        with open("media/" + str(file_id) + ".csv", "w", newline="") as csvf:

            writer = csv.DictWriter(
                csvf,
                fieldnames=names,
                delimiter=delimiter
            )
            writer.writeheader()

            for _ in range(rows):
                writer.writerow(
                    {
                        names[i]: genData(types[i], **additional_parameters[i])
                        for i in range(len(columns))
                    }
                )

        process.file_ready = True
        process.save()

    except AttributeError:
        print("There are no any work")
    else:
        print("New file was just created worked")


# celery worker -A project.celery -B
