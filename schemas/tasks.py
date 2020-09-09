from celery.task import periodic_task
from datetime import timedelta
from schemas.models import Processing, Schema
import csv
from faker import Faker


Faker.seed(0)
fake = Faker()


# fake generators
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


# Just convinient way to storage all in one
# **kwargs designed for additional_parameters dict in schema
# if it's necessary you can just add new add_param in that dict
# and handle them here(or not handle). it gonna work.
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


# this periodic task creates new csv files and save them in media dir
# to get new job it checks objects from Processing model
# with file_ready 'false" status
@periodic_task(run_every=timedelta(seconds=1), name="generate_file")
def build_csv_file():
    try:

        # extract all required data from Processing
        process = Processing.objects.filter(file_ready=False).first()
        file_id = process.file_id
        schema_id = process.schema_id
        rows = process.rows

        # extract data from schema, we gonna create files for
        schema = Schema.objects.get(id=schema_id)
        separator = schema.separator
        columns = schema.columns

        # replace all names,types,add_params in special lists
        # so that it was convinient to work with them
        names = [column["name"] for column in columns]
        types = [column["type"] for column in columns]
        additional_parameters = [
            column["additional_parameters"]
            for column in columns
        ]

        # determine required delimeter depends on data from form in frontend
        delimiter = {
            separator == "comma": ",",
            separator == "whitespace": " ",
            separator == "semicolon": ";",
        }[True]

        # create new csv file
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

        # label job as well done
        process.file_ready = True
        process.save()

    except AttributeError:
        print("There are no any work")
    else:
        print("New file was just created worked")


# to run: "celery worker -A project.celery -B"
