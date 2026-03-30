from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    station_1 = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        notes="Operational"
    )
    print(f"ID: {station_1.station_id}")
    print(f"Name: {station_1.name}")
    print(f"Crew: {station_1.crew_size} people")
    print(f"Power: {station_1.power_level}%")
    print(f"Oxygen: {station_1.oxygen_level}%")
    print(f"Status: "
          f"{'Operational' if station_1.is_operational else 'Offline'}")
    print("\n========================================")
    print("Expected validation error:")
    try:
        station_1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=70,
            power_level=85.5,
            oxygen_level=92.3,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
