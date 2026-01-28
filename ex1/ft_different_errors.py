def garden_operations():
    int("abc")
    1 / 0
    open("missing.txt")
    plant_dict = {
        1: "Rose",
        2: "Sunflower"
    }
    plant_dict[3]

def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
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
        print(f"aught FileNotFoundError: No such file '{name}'\n")

    try:
        print("Testing KeyError...")
        plant_dict = {
            1 : "Rose",
            2 : "Sunflower"
        }
        plant_dict[3]
    except KeyError:
        print("Caught KeyError: 'missing\_plant'\n")

    try:
        print("Testing multiple errors together...")
        garden_operations()
    except:
        print("Caught an error, but program continues!\n")
    
    print("All error types tested successfully!")

test_error_types()