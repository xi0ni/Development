#!/usr/bin/env python3

import csv

filepath = "/Users/georgerobokos/Development/Python/data/Cereal.csv"


with open(filepath, "r", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    cereals_data = list(csv_reader)


for row in cereals_data:
    print(row[0])

info = ""
while info != "stop":
    info = input(
        "type 'stop' to exit \nwhich would you like to know more about? "
    ).lower()

    if info == "stop":
        break

    found = False
    for row in cereals_data:
        if info in row[0].lower():
            found = True
            print(
                f"\n Name: {row[0]}\n Calories: {row[1]}\n Protein: {row[2]}\n Fat: {row[3]}"
                f"\n Carbohydrates: {row[4]}\n Sugar: {row[5]}\n Potassium: {row[6]}"
                f"\n Vitamins: {row[7]}\n Shelf: {row[8]}\n Weight: {row[9]}"
                f"\n Cups: {row[10]}\n Rating: {row[11]} \n"
            )
            change = input("\nWould you like to change any values? ").lower()

            if change in ("yes", "y"):
                value = (
                    input("Which value would you like to change? ").strip().capitalize()
                )
                if value in header:
                    new_val = input(f"Enter new value for {value}: ")
                    row[header.index(value)] = new_val
                    print("Value updated.")

                    with open(filepath, "w", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(header)
                        writer.writerows(cereals_data)
                        print("Changes saved to file.")
                else:
                    print("Invalid field name.")
            break

    if not found:
        print("Cereal not found.")
# hello
eorifewiorf

keprokfpoewrf
