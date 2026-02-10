def check_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temperature > 40:
        raise ValueError(
            f"{temperature}°C is too hot for plants "
            f"(max 40°C)")
    if temperature < 0:
        raise ValueError(
            f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]
    for value in tests:
        print(f"\nTesting temperature: {value}")
        try:
            temp = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as error:
            print(f"Error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
