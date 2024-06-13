import faker
import sqlite3
from random import choice


USERS_NUMBER = 30
TASKS_NUMBER = 60


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_tasks = []
    statuses = [("new",), ("in progress",), ("completed",)]

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append(
            (fake_data.name(), fake_data.unique.email(domain=fake_data.domain_name()))
        )

    for index in range(number_tasks):
        fake_tasks.append(
            (
                f"Task #{index+1}",
                choice([fake_data.text(max_nb_chars=100), None]),
                choice([1, 2, 3]),
                choice(range(1, number_users + 1)),
            )
        )

    return fake_users, fake_tasks, statuses


def insert_data_to_db(fake_users, fake_tasks, statuses):
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()

        sql_querry_for_status = "INSERT INTO status(name) VALUES (?)"
        cur.executemany(sql_querry_for_status, statuses)

        sql_querry_for_users = "INSERT INTO users(fullname, email) VALUES (?, ?)"
        cur.executemany(sql_querry_for_users, fake_users)

        sql_querry_for_tasks = (
            "INSERT INTO tasks(title, description, status_id, user_id) VALUES (?,?,?,?)"
        )
        cur.executemany(sql_querry_for_tasks, fake_tasks)

        con.commit()


if __name__ == "__main__":
    fake_users, fake_tasks, statuses = generate_fake_data(USERS_NUMBER, TASKS_NUMBER)
    insert_data_to_db(fake_users, fake_tasks, statuses)
