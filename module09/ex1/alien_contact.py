from typing import Annotated
from enum import Enum
from datetime import datetime
from sys import exit
try:
    from pydantic import BaseModel, Field, ValidationError, model_validator  # type: ignore
except ModuleNotFoundError:
    print("""
Could not import the pydantic module

Try 'pip install pydantic' in your environment
""")
    exit()


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: Annotated[str, Field(min_length=5, max_length=15)]
    timestamp: Annotated[datetime, Field(default=datetime.now())]
    location: Annotated[str, Field(min_length=3, max_length=100)]
    contact_type: Annotated[ContactType, Field()]
    signal_strength: Annotated[float, Field(ge=0.0, le=100.0)]
    duration_minutes: Annotated[int, Field(ge=1, le=1440)]
    witness_count: Annotated[int, Field(ge=1, le=100)]
    message_received: Annotated[str | None, Field()]
    is_verified: Annotated[bool, Field(default=False)]

    @model_validator(mode='after')
    def validate(self) -> "AlienContact":
        if self.contact_id[:3] != "AC":
            raise ValueError("Contact ID must start with 'AC'")
        elif self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        elif self.contact_type == ContactType.TELEPATHIC and self.witnesses < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must come in with a message")
        return self


def main() -> None:

    print(f"""Alien Contact Log Validation
{'=' * 40}
Valid contact report:
""")


if __name__ == "__main__":

