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
    CADET="cadet"
    OFFICER="officer"
    LIEUTENANT="lieutenant"
    CAPTAIN="captain"
    COMMANDER="commander"


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    rank: Annotated[Rank, Field()]
    age: Annotated[int, Field(ge=18, le= 80)]
    specialization: Annotated[str, Field(min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(ge=0, le=50)]


def main() -> None:
    ...


if __name__ == "__main__":
    main()
