from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 30
NUMBER_STATUS = 3
NUMBER_TASKS = 5

def generate_fake_data(number_users, number_status, number_tasks) -> tuple():
    fake_users = []# тут зберігатимемо юзерів
    fake_status = []# тут зберігатимемо статуси
    fake_tasks = []# тут зберігатимемо завдання
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''
    fake_data = faker.Faker()