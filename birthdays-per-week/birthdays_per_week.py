"""module with function get_birthdays_per_week"""

from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users):

    """function for birthday congratulation selection next week"""

    today = datetime.today().date()
    users_list = defaultdict(list)

    def sorted_by_date(user):
        return user["birthday"].date()

    users.sort(key=sorted_by_date)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days < 7:
            if birthday_this_year.weekday() > 4:
                if today.weekday() != 0:
                    users_list["Monday"].append(name)
            else:
                users_list[birthday_this_year.strftime("%A")].append(name)

    for weekday, name in users_list.items():
        print(f'{weekday}: {", ".join(name)}')

test_users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Nat Ku", "birthday": datetime(1977, 5, 31)},
    {"name": "Nik Kuch", "birthday": datetime(2007, 3, 3)},
    {"name": "Ro Curly", "birthday": datetime(2000, 2, 29)},
    {"name": "Lili Tod", "birthday": datetime(1971, 1, 20)},
    {"name": "Mike Red", "birthday": datetime(2001, 2, 28)},
    {"name": "Miky Green", "birthday": datetime(2001, 3, 1)},
    {"name": "Ron Kit", "birthday": datetime(1985, 3, 2)},
    {"name": "Rose Tick", "birthday": datetime(1979, 2, 25)},
    {"name": "Margo Tick", "birthday": datetime(1979, 2, 25)},
]

get_birthdays_per_week(test_users)
