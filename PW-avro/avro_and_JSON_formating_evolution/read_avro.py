import json
from avro.datafile import DataFileReader
from avro.io import DatumReader

input_file = "example_v2.avro"
output_file = "out.json"

records = []

# Open Avro file
with DataFileReader(open(input_file, "rb"), DatumReader()) as reader:
    for record in reader:
        records.append(record)

# Show JSON
print(json.dumps(records, indent=2))

# Save JSON
with open(output_file, "w") as f:
    json.dump(records, f, indent=2)

print("JSON written to", output_file)