from dotenv import load_dotenv
import os


def validate_vars(env_variables: dict[str, str | None]) -> bool:
    mandatory: set[str] = {"MATRIX_MODE",
                           "DATABASE_URL",
                           "API_KEY",
                           "LOG_LEVEL",
                           "ZION_ENDPOINT"}
    if not mandatory.issubset(env_variables):
        print("[WARNING] Missing key(s): "
              f"{mandatory - set(env_variables.keys())}")
        return False
    elif env_variables["MATRIX_MODE"] not in ["development", "production"]:
        print("\nThe value of [MATRIX_MODE] in the .env file can only be "
              "'development' or 'production'")
        return False
    for key in mandatory:
        if not env_variables[key]:
            print(f"\n[WARNING]: Missing value for '{key}'\n"
                  "Using default value")
    return True


def load_config(vars: dict[str, str | None]) -> bool:
    api_key = "0000007axel"
    log_level = "DEBUG"
    zion = "zion.endpoint"
    print("\nORACLE STATUS: Reading the Matrix...")
    if vars and validate_vars(vars):
        print(f"""
Configuration loaded:
Mode: {vars["MATRIX_MODE"]}
Database: Connected to {'local' if vars["MATRIX_MODE"] == "development"
                        else 'remote'} instance
API access: {'authenticated' if vars['API_KEY'] == api_key
             else 'unauthenticated'}
Log Level: {vars["LOG_LEVEL"] if vars["LOG_LEVEL"] else log_level}
Zion Network: {'ONLINE' if vars['ZION_ENDPOINT'] == zion else 'OFFLINE'}
""")
        return True
    else:
        print("The Matrix is not readable (invalid/missing .env file)")
        return False


if __name__ == "__main__":
    load_dotenv()
    global_vars = {}
    global_vars["MATRIX_MODE"] = os.getenv("MATRIX_MODE")
    global_vars["DATABASE_URL"] = os.getenv("DATABASE_URL")
    global_vars["API_KEY"] = os.getenv("API_KEY")
    global_vars["LOG_LEVEL"] = os.getenv("LOG_LEVEL")
    global_vars["ZION_ENDPOINT"] = os.getenv("ZION_ENDPOINT")
    valid = load_config(global_vars)
    if valid:
        if global_vars["MATRIX_MODE"] == "production":
            print("""
▄▖     ▌    ▗ ▘
▙▌▛▘▛▌▛▌▌▌▛▘▜▘▌▛▌▛▌
▌ ▌ ▙▌▙▌▙▌▙▖▐▖▌▙▌▌▌
                  """)
        else:
            print("""
▄       ▜            ▗
▌▌█▌▌▌█▌▐ ▛▌▛▌▛▛▌█▌▛▌▜▘
▙▘▙▖▚▘▙▖▐▖▙▌▙▌▌▌▌▙▖▌▌▐▖
            ▌
                  """)
    print("\nThe Oracle sees all configuration.")
