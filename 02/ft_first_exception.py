def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    for value in ['25', 'abc']:
        print(f"Input data is '{value}'")
        try:
            temp : int = input_temperature(value)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}\n")
        else:
            print(f"Temperature is now {temp}°C\n")


if __name__ == '__main__':
    test_temperature()
