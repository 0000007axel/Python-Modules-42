import importlib
from importlib.metadata import version
import sys


def version_checker(package: str) -> str:
    return version(package)


def import_checker(module: str) -> bool:
    module_description: str = 'Successfully imported the module'

    if module == "pandas":
        module_description = "Data manipulation ready"
    elif module == "numpy":
        module_description = "Numerical computation ready"
    elif module == "requests":
        module_description = "Newtork access ready"
    elif module == "matplotlib":
        module_description = "Visualisation ready"
    else:
        module_description = "Module imported successfully"
    try:
        importlib.import_module(module)
        print(f"[OK] {module} ({version_checker(module)}) - " + module_description)
        return True
    except ModuleNotFoundError:
        print(f"[FAILURE] - Failed to import module '{module}'")
        return False


if __name__ == "__main__":
    mandatory = ["pandas", "numpy", "requests", "matplotlib"]
    imported = []
    for module in mandatory:
        found = import_checker(module)
        if found:
            imported.append(module)
    if mandatory not in imported:
        sys.exit()

        

