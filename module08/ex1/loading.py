import importlib


def importer(modules: list[str]) -> None:
    for module in modules:
        try:
            mod = importlib.import_module(module)
            print(f"[OK] {module} ({mod.__version__}) - ", end="")
            if module == "pandas":
                print("Data manipulation ready")
            elif module == "numpy":
                print("Numerical computation ready")
            elif module == "requests":
                print("Newtork access ready")
            elif module == "matplotlib":
                print("Visualisation ready")
            else:
                print("Module imported successfully")

        except ModuleNotFoundError:
            print(f"[FAILURE] - Failed to import module '{module}'")


if __name__ == "__main__":
    importer(["pandas", "numpy", "requests", "matplotlib"])
