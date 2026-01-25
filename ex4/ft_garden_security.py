class SecurePlant:
    """
    Represents a plant with protected attributes and validation.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a SecurePlant instance.
        """
        self.name: str = name
        self._height: int = height
        self._age: int = age

    def set_height(self, height: int) -> None:
        """
        Update the plant's height if the value is valid.
        """
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        Update the plant's age if the value is valid.
        """
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """
        Returns the plant's current height.
        """
        return self._height

    def get_age(self) -> int:
        """
        Returns the plant's current age.
        """
        return self._age


if __name__ == "__main__":
    """
    Demonstrates secure updates to a plant's attributes and
    prevents invalid modifications.
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose
    print()
    print(
        f"Current plant: {rose.name} ({rose.get_height()}cm, "
        f"{rose.get_age()} days)"
    )
