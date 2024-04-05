import csv
from decimal import Decimal

def convert_weight(weight):
    print(f"Original weight: {weight}")
    return weight

def convert_dimensions(dimension):
    print(f"Original dimension: {dimension}")
    return dimension

def format_currency(currency):
    formatted_currency = round(Decimal(currency), 2)
    print(f"Formatted currency: {formatted_currency}")
    return formatted_currency

def read_homework():
    with open('homework.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        homework_data = [row for row in reader]
    return homework_data


def write_formatted(homework_data):
    headers = set()
    for row in homework_data:
        headers.update(row.keys())
        headers = sorted(list(headers))

    with open('formatted.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in homework_data:
            writer.writerow(row)

    print("Finished writing to formatted.csv")

homework_data = read_homework()
write_formatted(homework_data)
