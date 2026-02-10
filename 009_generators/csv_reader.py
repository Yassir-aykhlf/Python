def readCSV_gen(filename):
    try:
        with open(filename, 'r') as f:
            next(f)
            for line in f:
                yield line.strip().split(',')
    except FileNotFoundError:
        print(f"{filename} not found")
    except PermissionError:
        print(f"Permission denied for {filename}")

for row in readCSV("big_data.csv"):
    process(row)