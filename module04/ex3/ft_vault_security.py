def secure_archive(file_name: str,
                   action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, "r") as f:
                return (True, f.read())
        except Exception as e:
            return (False, f"{e}")
    elif action == "write":
        try:
            with open(file_name, "w") as f:
                f.write(content)
            with open(file_name, "r") as f:
                return (True, "Content successfully written to file")
        except Exception as e:
            print(f"{e}")
            return (False, "")
    else:
        print("Invalid argument(s)")
        return (False, "")


def main() -> None:
    print("=== Cyber archive Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"), "\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("hahah"), "\n")
    print("Using 'secure_archive' to read from a regular file:")
    file_content: tuple[bool, str] = secure_archive("test.txt")
    print(file_content, "\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", "write", file_content[1]))


if __name__ == "__main__":
    main()
