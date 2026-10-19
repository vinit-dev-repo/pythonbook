# workshop_schema_lab.py
from marshmallow import Schema, fields, post_load, ValidationError
from workshop_json_lab import CutPlan, MachineReport, document

class PlanSchema(Schema):
    day = fields.Date(required=True)
    metres = fields.Decimal(as_string=True, required=True)

    @post_load
    def make_plan(self, data, **kwargs):
        return CutPlan(**data)

class ReportSchema(Schema):
    recorded_at = fields.AwareDateTime(data_key="at", required=True)
    waste = fields.Decimal(as_string=True, required=True)

    @post_load
    def make_report(self, data, **kwargs):
        return MachineReport(**data)

class WorkshopSchema(Schema):
    plans = fields.List(fields.Nested(PlanSchema), required=True)
    reports = fields.List(fields.Nested(ReportSchema), required=True)

schema = WorkshopSchema()
encoded = schema.dumps(document)
loaded = schema.loads(encoded)
print("schema equal:", loaded == document)
print(type(loaded["plans"][0]).__name__, type(loaded["reports"][0]).__name__)
print(loaded["plans"][0].metres.as_tuple().exponent, loaded["reports"][0].waste.as_tuple().exponent)
print("external name:", "at" in schema.dump(document)["reports"][0])
try:
    schema.load({"plans": [], "reports": [{"at": "not a timestamp", "waste": "0"}]})
except ValidationError as error:
    print("nested error:", "reports" in error.messages)
