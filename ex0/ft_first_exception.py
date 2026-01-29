def check_temperature(tmp_str) -> int | None:
    try:
        temperature = int(tmp_str)
        if 0 <= temperature <= 40:
            return temperature
        elif temperature < 0:
            print(f"Error {temperature}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
    except ValueError:
        print(f"Error: '{tmp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature: 25")
    temp = check_temperature("25")
    print(f"Temperature {temp}°C is perfect for plants!\n")

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature("100")

    print("Testing temperature: -50")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")


test_temperature_input()
