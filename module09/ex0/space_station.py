from typing import Annotated
from datetime import date, datetime
try:
    from pydantic import BaseModel, Field
except ModuleNotFoundError:
    print("""
Could not import the pydantic module

Try 'pip install pydantic' in your environment
""")


class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(ge=1, le=20)]
    power_level: Annotated[float, Field(ge=0.0, le=100)]
    oxygen_level: Annotated[float, Field(ge=0.0, le=100)]
    last_maintenance: datetime
    is_operational: bool = True
    notes: Annotated[str | None, Field(max_length=200)]
