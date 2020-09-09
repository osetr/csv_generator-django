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
    return "".join([fake.sentence() for _ in range(number)])


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
        return genText(kwargs["text_sentences"])
    else:
        return genDate()


@periodic_task(run_every=timedelta(seconds=1), name="generate_file")
def build_csv_file():
    try:
        process = Processing.objects.first()
        file_id = process.file_id
        schema_id = process.schema_id
        rows = process.rows

        full_schema_info = list(Schema.objects.filter(id=schema_id).values())[0]

        schema_separator = full_schema_info["separator"]

        schema_columns = full_schema_info["columns"]

        columns_number = len(schema_columns)

        columns_names = [column["name"] for column in schema_columns]

        columns_types = [column["type"] for column in schema_columns]

        additional_parameters = [
            {"text_sentences": int(column["sentences_amount"])}
            if "sentences_amount" in column.keys()
            else {"another_parametr": 0}
            for column in schema_columns
        ]

        if schema_separator == "comma":
            delimiter = ","
        elif schema_separator == "whitespace":
            delimiter = " "
        else:
            delimiter = ";"

        with open("media/" + str(file_id) + ".csv", "w", newline="") as csvfile:

            writer = csv.DictWriter(
                csvfile, fieldnames=columns_names, delimiter=delimiter
            )
            writer.writeheader()

            for _ in range(rows):
                writer.writerow(
                    {
                        columns_names[i]: genData(
                            columns_types[i], **additional_parameters[i]
                        )
                        for i in range(columns_number)
                    }
                )

        process.delete()

    except AttributeError:
        print("There are no any work")
    else:
        print("New file was just created worked")


# celery worker -A project.celery -B
