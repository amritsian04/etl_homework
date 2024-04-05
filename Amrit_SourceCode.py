import csv
from decimal import Decimal

def convert_weight(weight):
    # Assuming the weight is in pounds or needs to be converted to pounds.
    # Implement conversion logic if needed.
    print(f"Original weight: {weight}")
    return weight

def convert_dimensions(dimension):
    # Assuming the dimension is in inches or needs to be converted to inches.
    # Implement conversion logic if needed.
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
    # Dynamically generate the list of headers from the keys present in all rows
    headers = set()
    for row in homework_data:
        headers.update(row.keys())
    
    # Convert the set of headers to a list (optional: sort the headers for consistency)
    headers = sorted(list(headers))

    with open('formatted.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in homework_data:
            writer.writerow(row)

    print("Finished writing to formatted.csv")

# Ensure the rest of your script correctly prepares homework_data
homework_data = read_homework()
write_formatted(homework_data)
