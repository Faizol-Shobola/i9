import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csv_filePath):

    # Open a csv reader called reader
    with open(csv_filePath, encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        data = []
        for row in csv_reader:
            team_name = row[0]
            series_number = row[1]
            file_name = row[2]
            name = row[3]
            description = row[4]
            gender = row[5]
            attribute = row[6]
            attributes_list = []
            attributes = attribute.split(";")
            print(attributes)
            for attr in attributes:
                attr_map = attr.split(":")
                attr_name = attr_map[0].strip()
                attr_value = attr_map[1].strip()
                attributes_list.append({"trait_type": attr_name, "value": attr_value})
                break
            id = row[7]

            # Convert each row into a dictionary and add it to data
            data.append({
                "format": "CHIP-007",
                "name": name,
                "description": description,
                "minting_tool": team_name,
                "sensitive_content": False,
                "series_number": series_number,
                "series_total": 420,
                "attributes": attributes_list,
                "collection": {
                    "name": "Zuri NFT Tickets for Free Lunch",
                    "id": id,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9."
                        }
                    ]
                }
            })

        # Open a json writer, and use the json.dumps() function to dump data
        with open('nft.json', 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        with open('nft.json', 'r') as jsonf:
            data = json.load(jsonf)

        with open('filename.output.csv', 'w') as f:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for name in data:
                writer.writerow(name)
            print('Done')


# Decide the csv file paths according to your computer system
get_csv = input('What is the name of the csv file ')
csv_filePath = get_csv

# Call the make_json function
make_json(csv_filePath)
