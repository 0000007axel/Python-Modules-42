def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        25 / 0
    elif operation_number == 2:
        open("nigga.txt", "r")
    elif operation_number == 3:
        25 + 'axl'
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except Exception as err:
            print(f"Caught {type(err).__name__}: {err}")
    print("\nAll error types completed successfully!")


if __name__ == "__main__":
    test_error_types()
