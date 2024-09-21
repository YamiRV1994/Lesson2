import csv

def main():
    # Создаем список словарей
    data = [
        {"name": "Вячеслав", "age": 30, "job": "Engineer"},
        {"name": "Игорь", "age": 25, "job": "Designer"},
        {"name": "Роман", "age": 35, "job": "Manager"},
        {"name": "Екатерина", "age": 28, "job": "Developer"}
    ]

    # Записываем данные в файл в формате CSV
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'age', 'job']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Записываем заголовок
        writer.writeheader()

        # Записываем каждый словарь в файл
        for row in data:
            writer.writerow(row)

    print("Данные успешно записаны в файл data.csv")

if __name__ == "__main__":
    main()