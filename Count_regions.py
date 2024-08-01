import json, sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print(f"Usage: python3 {sys.argv[0]} filename")
    exit()

with open(filename) as file:
    data = json.load(file)
if "_via_img_metadata" in data:
    print("Extracting annotations from project file.")
    data = data["_via_img_metadata"]
strings = []
for i in data.values():
    filename = i["filename"]
    num_regions = len(i["regions"])
    strings.append(f"File: {filename}\nRegions: {num_regions}")
print("\n".join(sorted(strings)))