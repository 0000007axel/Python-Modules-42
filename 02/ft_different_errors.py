def garden_operations(operations_number: int) -> None:

    if operations_number == 0:
        int("abc")

    elif operations_number == 1:
        25 / 0

    elif operations_number == 2:
        open("haha.txt", "r")

    elif operations_number == 3:
        25 + "abc"

    else:
        return



def test_error_types() -> None:
    print("==== Garden Error Types Demo ===")
    for i in range (0, 5):
        print(f"Testing with operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except Exception as err:
            print(f'Caught {err.__class__.__name__}: {err}')

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
