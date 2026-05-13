"""Space Crew module for validating mission crew assignments."""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    """Enumeration of crew member ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Model representing a crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(
        min_length=3, max_length=30
    )
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=None)


class SpaceMission(BaseModel):
    """Model representing a space mission with crew."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(
        min_length=3, max_length=100
    )
    destination: str = Field(
        min_length=3, max_length=50
    )
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(
        min_length=1, max_length=12
    )
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        """Validate mission business rules.

        Returns:
            Self if validation passes.

        Raises:
            ValueError: If any mission rule is violated.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with \"M\""
            )

        if not all(
            member.is_active for member in self.crew
        ):
            raise ValueError(
                "All crew members must be active"
            )

        ranks = {member.rank for member in self.crew}
        if not (
            Rank.CAPTIN in ranks
            or Rank.COMMANDER in ranks
        ):
            raise ValueError(
                "Mission crew must include at least "
                "one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions require at least "
                    "50% of crew with 5+ years of "
                    "experience"
                )

        return self


def main() -> None:
    """Demonstrate space mission crew validation."""
    print("Space Mission Crew Validation")
    print("=" * 41)
    try:
        crew_members = [
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=38,
                specialization="Mission Command",
                years_experience=12,
                is_active=True,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=34,
                specialization="Navigation",
                years_experience=6,
                is_active=True,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=31,
                specialization="Engineering",
                years_experience=4,
                is_active=True,
            ),
        ]
    except Exception:
        print("Error")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 7, 1),
            duration_days=900,
            crew=crew_members,
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except Exception as exc:
        print(
            "Validation error while creating "
            "valid mission:"
        )
        print(str(exc))
    print()
    print("=" * 41)
    try:
        SpaceMission(
            mission_id="M2025_PIONEER",
            mission_name="Forward Operating Post",
            destination="Ceres",
            launch_date=datetime(2025, 3, 1),
            duration_days=200,
            crew=[
                CrewMember(
                    member_id="C101",
                    name="Mira Patel",
                    rank=Rank.LIEUTENANT,
                    age=29,
                    specialization="Survey",
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C102",
                    name="Noah Ruiz",
                    rank=Rank.OFFICER,
                    age=37,
                    specialization="Science",
                    years_experience=8,
                    is_active=True,
                ),
            ],
            budget_millions=800.0,
        )
    except Exception as e:
        print("Validation error:")
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
