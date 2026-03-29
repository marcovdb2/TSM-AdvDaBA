## Install dependencies

Install the required package:

pip install avro-python3

## Run the program

First, generate the new Avro file:

python add_record.py

Then read the file:

python read_avro.py

## Description

The program creates a new Avro file (example_v2.avro) using an updated schema:

replaces date with time

keeps both fields as optional for compatibility

It copies old records and adds a new one with the new schema.

The reader prints the content in JSON format and saves it in out.json.


## Comment

I used a merged schema to keep both versions compatible in a single file.
This approach is simple and works well for this exercise.
In more advanced systems, multiple files (one per schema version) could also be used for better scalability.