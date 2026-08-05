from typing import Annotated
from datetime import datetime
from sys import exit
try:
    from pydantic import BaseModel, Field, ValidationError  # type: ignore
except ModuleNotFoundError:
    print("""
Could not import the pydantic module

Try 'pip install pydantic' in your environment
""")
    exit()


class SpaceStation(BaseModel):
    station_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=1, max_length=50)]
    crew_size: Annotated[int, Field(ge=1, le=20)]
    power_level: Annotated[float, Field(ge=0.0, le=100)]
    oxygen_level: Annotated[float, Field(ge=0.0, le=100)]
    last_maintenance: Annotated[datetime, Field()]
    is_operational: Annotated[bool, Field(default = True)]
    notes: Annotated[str | None, Field(max_length=200)]


def main() -> None:
    print(f"""
Space Station Data Validation
{'=' * 40}""")
    try:
        valid: SpaceStation = SpaceStation(station_id="ISS001",
                                           name="International Space Station",
                                           crew_size=6,
                                           power_level=85.5,
                                           oxygen_level=92.3,
                                           last_maintenance=datetime.now(),
                                           is_operational=True,
                                           notes="")
        print(f"""Valid station created:
ID: {valid.station_id}
Name: {valid.name}
Crew: {valid.crew_size} people
Power: {valid.power_level}%
Oxygen: {valid.oxygen_level}%
Status: {'Operational' if valid.is_operational else 'Non-Operational'}

{'=' * 40}""")
        invalid: SpaceStation = SpaceStation(station_id="S" * 7000,
                                             name="Intl Space Station",
                                             crew_size=50,
                                             power_level=85.5,
                                             oxygen_level=92.3,
                                             last_maintenance=datetime.now(),
                                             is_operational=True,
                                             notes="")
        print(invalid)
    except ValidationError as e:
        print("Caught validation error" + ("s" if len(e.errors()) > 1 else ""))
        for error in e.errors():
            print(error['loc'][0] + ": " + error['msg'])


if __name__ == "__main__":
    main()
