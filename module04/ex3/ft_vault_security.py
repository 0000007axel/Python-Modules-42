def secure_archive(filename: str, act: str = "r", s: str = "") -> tuple[bool, str]:
    try:
        if act == "r":
            with open(filename, "r") as file:
                return(True, file.read())
        elif act == "w":
            with open(filename, "w") as file:
                file.write(s)
                return(True, "Content successfully written to file")
        else:
            return(False, f"Invalid action {act}")
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        return (False, str(err))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print(f"""
Using 'secure_archive' to read from a nonexistant file:
{secure_archive("not/existing/file")}

Using 'secure_archive' to read from a inaccessible file:
{secure_archive("etc/master.passwd")}

Using 'secure_archive' to read from a regular file:
{secure_archive("haha.txt")}
""")
    print(f"""Using 'secure_archive' to write previous content to a new file:
{secure_archive("new_file", "w", secure_archive("haha.txt")[1])}""")


if __name__ == "__main__":
    main()
