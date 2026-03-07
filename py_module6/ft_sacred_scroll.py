import alchemy


if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===\n")
    try:
        print("Testing direct module access:")
        print(
            f"alchemy.elements.create_fire(): "
            f"{alchemy.elements.create_fire()}")
        print(
            f"alchemy.elements.create_water(): "
            f"{alchemy.elements.create_water()}")
        print(
            f"alchemy.elements.create_earth(): "
            f"{alchemy.elements.create_earth()}")
        print(
            f"alchemy.elements.create_air(): "
            f"{alchemy.elements.create_air()}")

        print("\nTesting package-level access (controlled by __init__.py):")
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.create_water(): {alchemy.create_water()}")

        try:
            alchemy.create_earth()
        except Exception:
            print("alchemy.create_earth(): AttributeError - not exposed")

        try:
            alchemy.create_air()
        except Exception:
            print("alchemy.create_air(): AttributeError - not exposed")

        print("\nPackage metadata:")
        print(f"Version: {alchemy.__version__}")
        print(f"Author: {alchemy.__author__}")
    except Exception as e:
        print(f"Error: {e}")
