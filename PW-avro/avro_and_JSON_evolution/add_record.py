import time
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import avro.schema

input_file = "example.avro"
output_file = "example_v2.avro"

# New merged schema:
# - old records can still keep "date"
# - new records can use "time"
# Both are optional so the file can contain both versions
new_schema_json = """
{
  "namespace": "advdaba",
  "type": "record",
  "name": "Conference",
  "fields": [
    { "name": "name", "type": "string" },
    { "name": "date", "type": ["null", "long"], "default": null },
    { "name": "time", "type": ["null", "long"], "default": null },
    { "name": "location", "type": "string" },
    { "name": "speakers", "type": {"type":"array","items":"string"} },
    { "name": "participants", "type": {"type":"array","items":"string"} },
    { "name": "seating", "type": {"type":"map","values":"int"} }
  ]
}
"""

new_schema = avro.schema.parse(new_schema_json)

# Create new file with the merged schema
with DataFileWriter(open(output_file, "wb"), DatumWriter(), new_schema) as writer:
    # Copy old records into the new file
    with DataFileReader(open(input_file, "rb"), DatumReader()) as reader:
        for record in reader:
            new_record = {
                "name": record["name"],
                "date": record["date"],   # old field kept
                "time": None,             # new field missing in old records
                "location": record["location"],
                "speakers": record["speakers"],
                "participants": record["participants"],
                "seating": record["seating"]
            }
            writer.append(new_record)

    # Add one new record using "time" instead of "date"
    writer.append({
        "name": "Conference 2026",
        "date": None,
        "time": int(time.time() * 1000),   # current timestamp in ms
        "location": "Lausanne",
        "speakers": ["Alice", "Bob"],
        "participants": ["Marco", "Safia"],
        "seating": {
            "Alice": 1,
            "Bob": 2,
            "Marco": 10,
            "Safia": 11
        }
    })

print("New Avro file created:", output_file)