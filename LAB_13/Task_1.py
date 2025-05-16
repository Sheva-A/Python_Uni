import json
import tkinter as tk
from tkinter import ttk, messagebox

# Завантаження JSON
def load_data():
    with open("iphones.json", "r", encoding="utf-8") as file:
        return json.load(file)

phones = load_data()

# Сортування
def sort_phones(key):
    global phones
    phones = sorted(phones, key=lambda x: x[key], reverse=True)
    update_listbox()

# Пошук
def search_phones():
    query = search_entry.get().lower()
    results = [p for p in phones if query in p["name"].lower() or query in p["details"].lower()]
    update_listbox(results)

# Оновлення списку
def update_listbox(data=None):
    listbox.delete(0, tk.END)
    data = data or phones
    for phone in data:
        listbox.insert(tk.END, phone["name"])

# Показати деталі
def show_details(event):
    selected_index = listbox.curselection()
    if not selected_index:
        return
    phone = phones[selected_index[0]]
    info = f"{phone['name']}\nЦіна: {phone['price']} грн\nРейтинг: {phone['rating']}\nВідгуки: {phone['reviews']}\nХарактеристики: {phone['details']}"
    messagebox.showinfo("Деталі", info)

# GUI
root = tk.Tk()
root.title("Перегляд iPhone")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

search_entry = ttk.Entry(frame)
search_entry.pack(fill=tk.X, pady=5)
ttk.Button(frame, text="Пошук", command=search_phones).pack()

sort_frame = ttk.Frame(frame)
sort_frame.pack(pady=5)

ttk.Button(sort_frame, text="Сортувати за ціною", command=lambda: sort_phones("price")).pack(side=tk.LEFT, padx=2)
ttk.Button(sort_frame, text="Сортувати за рейтингом", command=lambda: sort_phones("rating")).pack(side=tk.LEFT, padx=2)
ttk.Button(sort_frame, text="Сортувати за відгуками", command=lambda: sort_phones("reviews")).pack(side=tk.LEFT, padx=2)

listbox = tk.Listbox(frame, height=10)
listbox.pack(fill=tk.BOTH, expand=True, pady=5)
listbox.bind("<<ListboxSelect>>", show_details)

update_listbox()

root.mainloop()
