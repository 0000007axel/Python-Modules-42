def input_temperature(temp_str: str) -> int:
    if int(temp_str) > 40:
        raise ValueError(f'{temp_str}°C is too hot for plants (max 40°C)')
    elif int(temp_str) < 0:
        raise ValueError(f'{temp_str}°C is too cold for plants (min 0°C)')
    else:
        return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    for value in ['25', 'abc', '100', '-50']:
        print(f"Input data is '{value}'")
        try:
            temp : int = input_temperature(value)
        except ValueError as err:
            print(f"Caught input_temperature error: {err}\n")
        else:
            print(f"Temperature is now {temp}°C\n")
    print('All tests completed - program didn\'t crash!')



if __name__ == '__main__':
    test_temperature()
