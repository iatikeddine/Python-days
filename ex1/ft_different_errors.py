def garden_operations(error_type: str) -> None:
    if error_type == "ValueError":
        int("abc")

    elif error_type == "ZeroDivisionError":
        1 / 0

    elif error_type == "FileNotFoundError":
        open("missing.txt", "r")

    elif error_type == "KeyError":
        plant_dict = {
            1: "Rose",
            2: "Sunflower"
        }
        plant_dict[3]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        1 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
