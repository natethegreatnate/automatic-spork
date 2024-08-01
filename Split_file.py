import json, sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print(f"Usage: python3 {sys.argv[0]} filename")
    exit()
with open(filename) as file:
    data = json.load(file)

for i in data:
    with open("Split_"+data[i]['filename']+"_.json", "w") as file:
        json.dump({i:data[i]}, file)