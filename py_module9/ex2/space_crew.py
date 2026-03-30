from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        ranks = [member.rank for member in self.crew]
        if Rank.COMMANDER not in ranks and Rank.CAPTAIN not in ranks:
            raise ValueError("Mission must have at least one Commander or "
                             "Captain")
        experienced = sum(1 for member in self.crew
                          if member.years_experience >= 5)
        if self.duration_days > 365 and (experienced / len(self.crew)) < 0.5:
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    member_1 = CrewMember(
        member_id="C11",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=45,
        specialization="Mission Command",
        years_experience=20
    )
    member_2 = CrewMember(
        member_id="C22",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=60,
        specialization="Navigation",
        years_experience=40
    )
    member_3 = CrewMember(
        member_id="C33",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=25,
        specialization="Engineering",
        years_experience=7
    )
    mission_1 = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        crew=[member_1, member_2, member_3],
        budget_millions=2500.0
    )
    print(f"Mission: {mission_1.mission_name}")
    print(f"ID: {mission_1.mission_id}")
    print(f"Destination: {mission_1.destination}")
    print(f"Duration: {mission_1.duration_days} days")
    print(f"Budget: ${mission_1.budget_millions}M")
    print(f"Crew size: {len(mission_1.crew)}")
    print("Crew members:")
    print(f"{member_1.name} ({member_1.rank.value}) - "
          f"{member_1.specialization}")
    print(f"{member_2.name} ({member_2.rank.value}) - "
          f"{member_2.specialization}")
    print(f"{member_3.name} ({member_3.rank.value}) - "
          f"{member_3.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission_2 = SpaceMission(
            mission_id="M2025_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=700,
            crew=[member_2, member_3],
            budget_millions=4000.0)
        print(mission_2)
    except ValidationError as e:
        print(e.errors()[0]["msg"][13:])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
