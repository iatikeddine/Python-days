def garden_operations() -> None:
    try:
        int("abc")
    except ValueError:
        print("ValueError demonstrated")
    try:
        1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError demonstrated")
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("FileNotFoundError demonstrated")
    try:
        plant_dict = {
            1: "Rose",
            2: "Sunflower"
        }
        plant_dict[3]
    except KeyError:
        print("KeyError demonstrated")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        name = "missing.txt"
        open(name, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{name}'\n")

    try:
        print("Testing KeyError...")
        plant_dict = {
            1: "Rose",
            2: "Sunflower"
        }
        plant_dict['missing\_plant']
    except KeyError:
        print("Caught KeyError: 'missing\_plant'\n")

    try:
        print("Testing multiple errors together...")
        1 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
