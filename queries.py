import sqlite3


def execute_query(sql, parameters=[]):
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        cur.execute(sql, parameters)

        return cur.fetchall()
    
'Отримати всі завдання певного користувача'
def get_all_task_by_id(user_id):
    query =  'SELECT * FROM tasks WHERE user_id = ?;'

    return execute_query(query, [str(user_id)])

'Вибрати завдання за певним статусом'
def get_task_by_status(status):
    query = "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?);"

    return execute_query(query, [status])
    

'Оновити статус конкретного завдання'
def update_task_status(task_id, status):
    query = "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = ?) WHERE id = ?;"
    
    return execute_query(query,[status,str(task_id)] )


'Отримати список користувачів, які не мають жодного завдання.'
def get_users_without_tasks():
    query = "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);"

    return execute_query(query)


'Додати нове завдання для конкретного користувача'
def add_task_to_user(user_id, title, task):
    query = "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, (SELECT id FROM status WHERE name = 'new'), ?);"

    return execute_query(query, [title, task, user_id])

'Отримати всі завдання, які ще не завершено:'
def tasks_not_finished_yet():
    qeury = "SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');"

    return execute_query(qeury)


'Видалити конкретне завдання'
def delete_the_task(task_id):
    query = "DELETE FROM tasks WHERE id = ?;"

    return execute_query(query, [task_id])

'Знайти користувачів з певною електронною поштою'
def find_user_by_email(domain):
    query = "SELECT * FROM users WHERE email LIKE ?;"

    return execute_query(query, [f"%@{domain}"])

"Оновити ім'я користувача"
def users_name_update(user_id, new_name):
    query = "UPDATE users SET fullname = ? WHERE id = ?;"

    return execute_query(query, [new_name, user_id])


'Отримати кількість завдань для кожного статусу'
def get_numbers_of_task_by_status():
    query = """
    SELECT s.name, COUNT(t.id) AS task_count
    FROM status s
    LEFT JOIN tasks t ON s.id = t.status_id
    GROUP BY s.name;
    """

    return execute_query(query)

"Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти"
def get_task_by_email(domain):
    query = """
    SELECT t.*
    FROM tasks t
    JOIN users u ON t.user_id = u.id
    WHERE u.email LIKE ?;
    """
    return execute_query(query, [f"%@{domain}"])

"Отримати список завдань, що не мають опису"
def get_tasks_without_description():
    query = "SELECT * FROM tasks WHERE description IS NULL OR description = '';"

    return execute_query(query)


"Вибрати користувачів та їхні завдання, які є у статусі 'in progress'"
def get_users_with_in_progress_status():
    query = """
    SELECT u.fullname, t.title, t.description
    FROM users u
    JOIN tasks t ON u.id = t.user_id
    JOIN status s ON t.status_id = s.id
    WHERE s.name = 'in progress';
    """

    return execute_query(query)

"Отримати користувачів та кількість їхніх завдань"
def get_users_and_numbers_of_task():
    query = """
    SELECT u.fullname, COUNT(t.id) AS task_count
    FROM users u
    LEFT JOIN tasks t ON u.id = t.user_id
    GROUP BY u.id;
    """
    return execute_query(query)


if __name__ == "__main__":
    # print(get_all_task_by_id(7))
    # print(get_task_by_status('new'))
    # print(update_task_status(10, 'new'))
    # print(get_users_without_tasks())
    # print(add_task_to_user(10, 'Create a db', 'Should be done by deadline'))
    # print(tasks_not_finished_yet())
    # print(delete_the_task(58))
    # print(find_user_by_email('mays.com'))
    # print(users_name_update(31, 'Dmytro'))
    # print(get_numbers_of_task_by_status())
    # print(get_task_by_email('morris.com'))
    # print(get_tasks_without_description())
    # print(get_users_with_in_progress_status())
    print(get_users_and_numbers_of_task())

