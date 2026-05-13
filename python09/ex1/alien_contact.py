"""Alien Contact module for validating alien contact reports."""

from datetime import datetime
from enum import Enum
from typing import Optional
from typing_extensions import Self

from pydantic import BaseModel, Field, model_validator


class ContactType(Enum):
    """Enumeration of possible contact types."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Model representing an alien contact report."""

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(
        default=None, max_length=500
    )
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def rule_validation(self) -> Self:
        """Validate business rules for alien contacts.

        Returns:
            Self if validation passes.

        Raises:
            ValueError: If any business rule is violated.
        """
        if not (self.contact_id[0:2].lower() == "ac"):
            raise ValueError(
                "contact_id must start with 'AC'"
            )
        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least "
                "3 witnesses"
            )
        if (
            self.signal_strength > 7.0
            and not self.message_received
        ):
            raise ValueError(
                "Strong signals should include a "
                "received message"
            )
        return self


def main() -> None:
    """Demonstrate alien contact log validation."""
    print("Alien Contact Log Validation")
    print("=" * 40)
    try:
        sample_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 11, 4, 21, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        message_text = sample_contact.message_received
        if message_text is None:
            message_text = "<no message>"
        else:
            message_text = f"'{message_text}'"

        lines = [
            "Valid contact report:",
            f"ID: {sample_contact.contact_id}",
            f"Type: {sample_contact.contact_type.value}",
            f"Location: {sample_contact.location}",
            f"Signal: {sample_contact.signal_strength}/10",
            (
                "Duration: "
                f"{sample_contact.duration_minutes} minutes"
            ),
            f"Witnesses: {sample_contact.witness_count}",
            f"Message: {message_text}",
        ]

        print("\n".join(lines))
    except Exception as e:
        print(
            "Validation error:\n"
            f"{e.errors()[0]['msg']}"
        )
    print()
    print("=" * 40)
    try:
        AlienContact(
            contact_id="AC_TS_007",
            timestamp=datetime.now(),
            location="Deep Space Relay",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.0,
            duration_minutes=5,
            witness_count=2,
            message_received="",
            is_verified=True,
        )
    except Exception as e:
        print(
            "Validation error:\n"
            f"{e.errors()[0]['msg']}"
        )


if __name__ == "__main__":
    main()
