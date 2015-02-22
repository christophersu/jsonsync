import json

# Syncs a JSON file with a Python dictionary
def sync(json_filename, data):
    json_file = open(json_filename)
    json_data = json.load(json_file)
    json_file.close()

    for key in data:
        json_data[key] = data[key]

    with open(json_filename, 'w') as outfile:
        json.dump(json_data, outfile)