def input_temperature(temp_str : str) -> int:
    int_temp : int = int(temp_str)
    if int_temp < 0:
        raise ValueError(f"{int_temp}°C is too cold for plants (min 0°C)")
    if int_temp > 40:
        raise ValueError(f"{int_temp}°C is too hot for plants (max 40°C)")

    return (int_temp)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    for i in ['25', 'abc', '100', '-50']:
        print(f"Input data is '{i}'")
        try:
            temperature : int = input_temperature(i)
            print(f"Temperature is now {temperature}°C\n")
        except Exception as err:
            print(f"Caught input_temperature error: {err}\n")
    print("All tests completed - program didn't crash!")

if __name__ == '__main__':
    test_temperature()
