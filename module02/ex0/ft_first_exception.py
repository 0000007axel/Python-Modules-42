def input_temperature(temp_str: str) -> int:
    int_temp: int = int(temp_str)
    return (int_temp)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    for i in ['25', 'abc']:
        print(f"Input data is '{i}'")
        try:
            temperature: int = input_temperature(i)
            print(f"Temperature is now {temperature}°C\n")
        except Exception as err:
            print(f"Caught input_temperature error: {err}\n")
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
