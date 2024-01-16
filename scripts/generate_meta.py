import pathlib
import json
from pathlib import Path

json_path = "../AllIconNames.json"


pngs = sorted(Path("../png").glob("*.png"))
svgs = sorted(Path("../svg").glob("*.svg"))

def map_name(file):
    return file.name

output = {
    "png": list(map(map_name, pngs)),
    "svg": list(map(map_name, svgs))
}

# Write the new file
with open(json_path, "w", encoding="UTF-8") as f:
    json.dump(output, f, indent=2, sort_keys=True)
    f.write("\n")

print("Done!")
print("Please commit the new AllIconNames.json file.")
