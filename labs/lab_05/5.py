N = int(input("How many files? "))

with open("output/multiple_out.txt", "w+") as out:
    for i in range(1, N + 1):
        mult_file = "input/multiple" + str(i) + ".txt"
        with open(mult_file, "r") as infile:
            out.write(infile.read())
