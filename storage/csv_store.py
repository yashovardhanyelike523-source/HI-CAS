import csv

def save_consumption(logs):
    with open("consumption.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Used"])

        for log in logs:
            writer.writerow([log.name, log.used])