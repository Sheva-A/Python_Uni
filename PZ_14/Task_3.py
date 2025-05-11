import json
import os

DB_FILE = 'clients.json'

def load_db():
    """Завантаження бази даних із JSON-файлу, якщо він існує"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(clients):
    """Збереження бази даних у JSON-файл"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(clients, f, ensure_ascii=False, indent=4)

def add_client(name, email):
    """Додавання нового клієнта"""
    db = load_db()
    db.append({'name': name, 'email': email})
    save_db(db)
    print(f"Клієнта {name} додано.")

def find_client(name):
    """Пошук клієнта за ім'ям"""
    results = [client for client in load_db() if client['name'] == name]
    if results:
        print(f"Клієнта {name} знайдено: {results}")
    else:
        print(f"Клієнта {name} не знайдено.")
    return results

def update_client(name, new_email):
    """Оновлення електронної пошти клієнта"""
    db = load_db()
    found = False
    for client in db:
        if client['name'] == name:
            client['email'] = new_email
            found = True
            break
    if found:
        save_db(db)
        print(f"Клієнта {name} оновлено: новий email {new_email}")
    else:
        print(f"Клієнта {name} не знайдено. Оновлення не виконано.")

def delete_client(name):
    """Видалення клієнта з бази"""
    db = load_db()
    initial_len = len(db)
    db = [client for client in db if client['name'] != name]
    if len(db) < initial_len:
        save_db(db)
        print(f"Клієнта {name} видалено.")
    else:
        print(f"Клієнта {name} не знайдено. Видалення не виконано.")


add_client("Олексій", "oleksii@example.com")
update_client("Олексій", "oleksiy@newmail.com")
find_client("Олексій")
delete_client("Олексій")
find_client("Олексій")
