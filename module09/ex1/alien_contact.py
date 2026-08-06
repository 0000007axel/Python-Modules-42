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
    signal_strength: Annotated[float, Field(ge=0.0, le=10.0)]
    duration_minutes: Annotated[int, Field(ge=1, le=1440)]
    witness_count: Annotated[int, Field(ge=1, le=100)]
    message_received: Annotated[str | None, Field()]
    is_verified: Annotated[bool, Field(default=False)]

    @model_validator(mode='after')
    def validate(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC'")
        elif self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        elif self.contact_type == ContactType.TELEPATHIC and self.witnesses < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must come in with a message")
        return self

def main():
    print(f"Alien Contact Log Validation\n{'=' * 40}")
    try:
        valid: AlienContact = AlienContact(contact_id="AC_2024_01",
                                           location="Area 51, Nevada",
                                           contact_type=ContactType.RADIO,
                                           signal_strength=8.5,
                                           duration_minutes=45,
                                           witness_count=5,
                                           message_received="Greetings UwU"
                                           )
        print(f"""
Valid Contact report:
ID: {valid.contact_id}
Type: {valid.contact_type}
Location: {valid.location}
Signal: {valid.signal_strength}
Duration: {valid.duration_minutes}
Witnesses: {valid.witness_count}
Message: {valid.message_received}
""")
    except ValidationError as e:
        print("Caught validation error" + ("s" if e.error_count() > 1 else ""))
        for error in e.errors():
            print(error['loc'][0] + ": " + error['msg'])
    print(f"\n{'=' * 40}")
    try:
        invalid: AlienContact = AlienContact(contact_id="AC_2024_01",
                                           location="Area 51, Nevada",
                                           contact_type=ContactType.RADIO,
                                           signal_strength=9000,
                                           duration_minutes=45,
                                           witness_count=5,
                                           message_received="Greetings UwU"
                                           )
        print(f"""Alien Contact Log Validation
{'=' * 40}
Valid Contact report:
ID: {invalid.contact_id}
Type: {invalid.contact_type}
Location: {invalid.location}
Signal: {invalid.signal_strength}
Duration: {invalid.duration_minutes}
Witnesses: {invalid.witness_count}
Message: {invalid.message_received}
""")
    except ValidationError as e:
        print("Expected validation error" + ("s:" if e.error_count() > 1 else ":"))
        for error in e.errors():
            print(error['loc'][0] + ": " + error['msg'])




if __name__ == "__main__":
    main()
