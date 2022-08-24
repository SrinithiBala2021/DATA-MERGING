import csv

data = []

with open("data.csv" , "r")as f:
    csv_reader  = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
star_data = data[1:]

with open("data_sorted.csv" , "a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

with open("data_sorted.csv")as input,open("data_sorted1.csv" , "w" , newline = "")as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row ):
            writer.writerow(row)
        
