import csv

# hw_200.csv:
# height and weight for 200 individuals Each record includes 3 values: index,
# height (inches), weight (pounds). There is also an initial header line

with open("input/hw_200.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    data = list(reader)
    # Calculate Height/Weight Ratio
    data[0].append('"Height/Weight Ratio (in/lb)"')
    for i in range(1, len(data)):
        row = data[i]
        ratio = round(((float(row[1]) / float(row[2])) * 100), 2)
        row.append(" " + str(ratio))
        data[i] = row

with open("output/hw_200_modified.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
