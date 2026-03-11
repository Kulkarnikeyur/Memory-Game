import csv

def save_score(name, moves,time_taken):
    K = 1
    with open("data/record.csv", "r") as A:
        csv_reader = csv.reader(A)
        next(csv_reader)
        for i in csv_reader:
            K += 1
    with open("data/record.csv", "a") as A:
        A.write(f"{K},{name},{moves},{time_taken}\n")
