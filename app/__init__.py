import csv
from flask import Flask, jsonify, request
app = Flask(__name__, static_folder=None)


@app.route("/count")
def count():
    with open('dogs_of_nyc_ wnyc.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        query_params = list(map(lambda x: x.lower(), request.args.keys()))
        invalid_params = set(query_params).difference(reader.fieldnames)

        if (len(invalid_params) > 0):
            unknown_fields = list(invalid_params)
            unknown_fields.sort()

            return jsonify({"unknown fields": unknown_fields}), 400

        count = 0

        for row in reader:
            if all(row_match(key, value, row) for key, value in request.args.items()):
                count += 1

        return jsonify({"count": count})


def row_match(key, value, row):
    key = key.lower()

    # Parse and compare `zip_code`
    if key == 'zip_code':
        query_zip = int(value)
        row_zip = int(row[key])

        if query_zip == row_zip:
            return True
    # The rest are strings
    elif row[key].lower() == value.lower():
        return True

    return False
