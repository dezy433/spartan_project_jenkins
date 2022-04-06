from flask import request
from spartan import Spartan
from pymongo import MongoClient
import time

while True:
    try:
        client = MongoClient("mongodb://db.deren.devops106:27017")
        break
    except Exception as e:
        print("Trying to make a connection to the database")
        time.sleep(2)

db = client.spartans

# all_spartans_db = {}



def spartan_info(spartan_id_to_display):
    spartan_id = int(spartan_id_to_display)
    record_search_result = db.clients_data.find({"sparta_id": spartan_id})
    search_result_list = list(record_search_result)
    if len(search_result_list) > 0:
        spartan_details = search_result_list[0]
        return f"ID found with following details:\n{spartan_details}"
    return f"ID not found."


def read_spartan_from_json():
    if request.is_json:
        trainee_data = request.get_json()

        if len(trainee_data["first_name"]) > 1:
            s_first_name = trainee_data["first_name"]
        else:
            return "First name should be at least 2 characters"

        if len(trainee_data["last_name"]) > 1:
            s_last_name = trainee_data["last_name"]
        else:
            return "Last name should have at least 2 characters"

        if int(trainee_data["birth_day"]) in range(1, 32):
            s_birth_day = trainee_data["birth_day"]
        else:
            return "Birth day should be a number between 1 and 31."

        if int(trainee_data["birth_month"]) in range(1, 13):
            s_birth_month = trainee_data["birth_month"]
        else:
            return "Birth Month should be between 1 and 12."

        if int(trainee_data["birth_year"]) in range(1900, 2005):
            s_birth_year = trainee_data["birth_year"]
        else:
            return "Birth Year should between 1900 and 2004"

        if len(trainee_data["s_course"]) > 1:
            s_course = trainee_data["s_course"]
        else:
            return "Course name is required to have at least 2 characters"

        if len(trainee_data["s_stream"]) > 1:
            s_stream = trainee_data["s_stream"]
        else:
            return "Stream name is required to have at least 2 characters"
        if check_id_in_db(trainee_data["sparta_id"]):
            return "ID already exists"
        else:
            s_id = trainee_data["sparta_id"]
        trainee = Spartan(s_id, s_first_name, s_last_name, s_birth_day, s_birth_month, s_birth_year, s_course, s_stream)
        return trainee
    else:
        return None


def add_to_db():
    spartan = read_spartan_from_json()

    if spartan is None:

        return "Please add the employee details"

    elif type(spartan) is str:

        return f"{spartan}"

    else:

        record = db.clients_data.insert_one(vars(spartan))
        return f"Entry saved{record}."


def check_id_in_db(id_to_check):
    records = db.clients_data.find({"sparta_id": id_to_check})
    data = list(records)
    return len(data) > 0


def display_db():
    data_list = list(db.clients_data.find())
    result = ""
    for entry in data_list:
        result += f"{entry}\n\n"
    return result
