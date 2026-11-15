
# Reflection Question 1:
# Python makes it easier to automate the process of reading,
# changing, and writing large amounts of data without manually
# repeating the same steps. Excel is better for visually looking
# at data and making quick changes without having to write code.

# Reflection Question 2:
# A business could use an append mode log file to keep track
# of its daily sales revenue. Append mode would allow the
# business to add new sales records without deleting any
# of the previous records.

import csv
from datetime import datetime

# Exercise 1 - Get the file
print("Exercise 1")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    rows = list(reader)

    print("Header:", header)
    print("Number of data rows:", len(rows))


# Exercise 2 - Read and print raw rows
print("\nExercise 2")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3 - Skip the header
print("\nExercise 3")

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4 - Compute totals
print("\nExercise 4")

total_revenue = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5 - Filter and write
print("\nExercise 5")

original_count = 0
written_count = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            original_count += 1

            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                written_count += 1

print(f"Rows written: {written_count} out of {original_count}")


# Exercise 6 - csv.DictReader
print("\nExercise 6")

# I would use csv.reader for simple files with a known column order.
# I would use DictReader when accessing columns by name is easier.

dict_total = 0

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        dict_total += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")
print("Totals match:", round(dict_total, 2) == round(total_revenue, 2))


# Exercise 7 - Sales summary by product
print("\nExercise 7")

summary = {}

with open("data/sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity

        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


# Exercise 8 - Append mode log
print("\nExercise 8")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as file:
    file.write(f"{timestamp} - Total revenue: ${total_revenue:.2f}\n")

print("Revenue added to run_log.txt")
