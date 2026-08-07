from typing import Annotated
from sys import exit
from enum import Enum
from datetime import datetime
try:
    from pydantic import (BaseModel,
                          Field,
                          ValidationError,
                          model_validator)
except ModuleNotFoundError:
    print("""
Could not import the pydantic module

Try 'pip install pydantic' in your environment
""")
    exit()


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    rank: Annotated[Rank, Field()]
    age: Annotated[int, Field(ge=18, le=80)]
    specialization: Annotated[str, Field(min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(ge=0, le=50)]
    is_active: Annotated[bool, Field(default=True)]


class SpaceMission(BaseModel):
    mission_id: Annotated[str, Field(min_length=5, max_length=15)]
    mission_name: Annotated[str, Field(min_length=3, max_length=100)]
    destination: Annotated[str, Field(min_length=3, max_length=50)]
    launch_date: Annotated[datetime, Field()]
    duration_days: Annotated[int, Field(ge=1, le=3650)]
    crew: Annotated[list[CrewMember], Field(min_length=1, max_length=12)]
    mission_status: Annotated[str, Field(default="planned")]
    budget_millions: Annotated[float, Field(ge=1.0, le=10000.0)]

    @model_validator(mode="after")
    def validate_crew(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError("Mission ID must start with 'M'")
        has_high_rank: bool = False
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                has_high_rank = True
                break
        if not has_high_rank:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")
        if self.duration_days >= 365:
            experienced_members: int = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_members += 1
            if experienced_members < len(self.crew) // 2:
                raise ValueError("More than half of the crew members"
                                 "are not experienced enough")
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"The crew member {member.name}"
                                 " is not active")
        return self


def main() -> None:
    print(f"Space Mission Crew Validation\n{'='*40}")
    try:
        new_crew = [CrewMember(member_id="SARAH25",
                               name="Sarah Connor",
                               rank=Rank.OFFICER,
                               age=22,
                               specialization="Mission Command",
                               years_experience=10,
                               is_active=True),
                    CrewMember(member_id="JOHN25",
                               name="John Smith",
                               rank=Rank.LIEUTENANT,
                               age=40,
                               specialization="Navigation",
                               years_experience=36,
                               is_active=True),
                    CrewMember(member_id="ALICE25",
                               name="Alice Johnson",
                               rank=Rank.OFFICER,
                               age=38,
                               specialization="Engineering",
                               years_experience=22,
                               is_active=True)]
        valid: SpaceMission = SpaceMission(mission_id="M2024_MARS",
                                           mission_name="Mars Colony Estab.",
                                           destination="Mars",
                                           launch_date=datetime.now(),
                                           duration_days=900,
                                           budget_millions=2500.0,
                                           crew=new_crew,
                                           mission_status="Okay UwU")
        print(f"""Valid mission created:
Mission: {valid.mission_name}
ID: {valid.mission_id}
Destination: {valid.destination}
Duration: {valid.duration_days} days
Budget: ${valid.budget_millions}M
Crew size: {len(valid.crew)}
Crew members:""")
        for member in valid.crew:
            print(f" - {member.name} ({member.rank})"
                  f" - {member.specialization}")

    except ValidationError as e:
        print("Expected validation error" +
              ("s:" if e.error_count() > 1 else ":"))
        for error in e.errors():
            print(f"{error['loc'][0]}: {error['msg']}")
    print(f"\n{'='*40}")
    try:
        new_crew = [CrewMember(member_id="SARAH25",
                               name="Sarah Connor",
                               rank=Rank.OFFICER,
                               age=22,
                               specialization="Mission Command",
                               years_experience=10,
                               is_active=True),
                    CrewMember(member_id="JOHN25",
                               name="John Smith",
                               rank=Rank.LIEUTENANT,
                               age=40,
                               specialization="Navigation",
                               years_experience=36,
                               is_active=True),
                    CrewMember(member_id="ALICE25",
                               name="Alice Johnson",
                               rank=Rank.OFFICER,
                               age=38,
                               specialization="Engineering",
                               years_experience=22,
                               is_active=True)]
        invalid: SpaceMission = SpaceMission(mission_id="M2024_MARS",
                                             mission_name="Mars Colony Estab.",
                                             destination="Mars",
                                             launch_date=datetime.now(),
                                             duration_days=900,
                                             budget_millions=2500.0,
                                             crew=new_crew,
                                             mission_status="Okay UwU")
        print(f"""Valid mission created:
Mission: {invalid.mission_name}
ID: {invalid.mission_id}
Destination: {invalid.destination}
Duration: {invalid.duration_days} days
Budget: ${invalid.budget_millions}M
Crew size: {len(invalid.crew)}
Crew members:""")
        for member in invalid.crew:
            print(f" - {member.name} ({member.rank}) "
                  f"- {member.specialization}")
    except ValidationError as e:
        print("Expected validation error" +
              ("s:" if e.error_count() > 1 else ":"))
        for error in e.errors():
            print(str(error['ctx']['error']))


if __name__ == "__main__":
    main()
