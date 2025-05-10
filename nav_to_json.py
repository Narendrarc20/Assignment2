import json

data = []
with open("NAVAll.txt", "r") as file:
    for line in file:
        parts = line.strip().split(";")
        if len(parts) > 5 and parts[0].isdigit():
            data.append({"Scheme Name": parts[3], "Net Asset Value": parts[4]})

with open("schemes.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
