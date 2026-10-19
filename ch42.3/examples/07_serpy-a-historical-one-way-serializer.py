from pydantic import BaseModel, ConfigDict, Field, ValidationError

class FlexibleCount(BaseModel):
    count: int

class StrictCount(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    count: int = Field(ge=0)

print(FlexibleCount.model_validate({"count": "7", "note": "ignored"}).model_dump())
for data in ({"count": "7"}, {"count": True},
             {"count": -1}, {"count": 7, "note": "extra"}):
    try:
        StrictCount.model_validate(data)
    except ValidationError:
        print("rejected")
print(StrictCount.model_validate({"count": 0}).model_dump_json())
