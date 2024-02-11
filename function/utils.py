from datetime import date
from dateutil.relativedelta import relativedelta

month_names = {"01": "січня", "02": "лютого", "03": "березня", "04": "квітня", "05": "травня",
               "06": "червня", "07": "липня", "08": "серпня", "09": "вересня", "10": "жовтня",
               "11": "листопада", "12": "грудня"}


def today_date():
    today = date.today()
    d = today.strftime("%d.%m.%Y")
    return d


def year_from_today():
    y_from_today = date.today() + relativedelta(years=1)
    d = y_from_today.strftime("%d.%m.%Y")
    return d


def end_of_year():
    today = date.today()
    d = "31.12." + str(today.year)
    return d


def date_to_dict(today):
    date_list = today.split('.')
    today_d = {"dd": date_list[0],
               "mm": date_list[1],
               "yyyy": date_list[2]}
    return today_d


def name_split(user_info, return_name: str):
    full_name = user_info.split()
    if return_name == "first_name":
        return full_name[1]
    elif return_name == "last_name":
        return full_name[0]
    elif return_name == "surname":
        return full_name[2]


def name_cut(user_info, return_name: str):
    full_name = user_info.split()
    if return_name == "half_name":
        return full_name[1] + " " + full_name[0]
    elif return_name == "small_name":
        return " " + full_name[0] + " " + full_name[1][0].upper() + "." + full_name[2][0].upper() + "."


def car_quantity(user_info):
    for i in range(1, 20):
        if user_info.find(str(i) + ")") == -1:
            return i - 1


def car_data(user_info, car_quan):
    data = {}
    user_info = user_info.replace(")", ",")
    info = user_info.split(";")

    for i in range(car_quan):

        car = info[i].split(",")
        j = i + 1
        data["count" + str(j)] = car[0]
        data["number" + str(j)] = car[1]
        data["name" + str(j)] = car[2]
        data["year" + str(j)] = car[3]

    return data


def car_split(user_info):

    if user_info["second_car_data"] is None:
        car_info = user_info["fisrt_car_data"].replace(',', '').split()
    elif user_info["third_car_data"] is None:
        car_info = user_info["fisrt_car_data"].replace(',', '').split() + \
                   user_info["second_car_data"].replace(',', '').split()
    else:
        car_info = user_info["fisrt_car_data"].replace(',', '').split() +\
                   user_info["second_car_data"].replace(',', '').split() + \
                   user_info["third_car_data"].replace(',', '').split()
    return car_info


def is_man_for_fop(code: str):
    if int(code[8]) % 2 == 0:
        return False
    else:
        return True


def is_man_for_tov(full_name_info, path):
    full_name = full_name_info.split(" ")

    file = open(path, "r", encoding="utf-8")
    man_name = file.read()
    man_names = man_name.split(" ")

    for i in range(len(man_names)):
        for j in range(len(full_name)):
            if full_name[j].lower() == man_names[i].lower():
                return True

    return False


def is_woman_for_tov(full_name_info, path):
    full_name = full_name_info.split(" ")

    file_w = open(path, "r", encoding="utf-8")
    woman_name = file_w.read()
    woman_names = woman_name.split(" ")

    for i in range(len(woman_names)):
        for j in range(len(full_name)):
            if full_name[j].lower() == woman_names[i].lower():
                return True

    return False
