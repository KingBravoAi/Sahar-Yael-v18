backend/tests/test_schema_v18.py
import json, os, jsonschema

def test_blueprint_schema():
    schema = json.load(open("blueprint/sahar_yael_v18.schema.json"))
    bp = json.load(open("blueprint/sahar_yael_v18.json"))
    jsonschema.validate(bp, schema)

