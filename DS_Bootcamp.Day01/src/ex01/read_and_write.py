import csv

def read_and_write():
    with open("ds.csv", "r", newline="") as csvfile, open ("ds.tsv", "w", newline="") as tsvfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(tsvfile, delimiter="\t")
        for row in reader:
            writer.writerow(row)

if __name__ == '__main__':
    read_and_write()