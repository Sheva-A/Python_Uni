list1 = [4, 2, 7, 2, 9, 4]
list2 = [3, 7, 1, 4, 3]

unique1 = set(list1)
unique2 = set(list2)

combined = sorted(unique1.union(unique2))

if combined:
    print("Об'єднаний та відсортований список:", combined)
else:
    print("Результуючий список порожній.")
