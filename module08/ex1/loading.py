import importlib
from importlib.metadata import version


def ver_check(package: str) -> str:
    return version(package.split(".")[0])


def import_checker(module: str) -> object | None:
    module_description: str = 'Successfully imported the module'

    if module == "pandas":
        module_description = "Data manipulation ready"
    elif module == "numpy":
        module_description = "Numerical computation ready"
    elif module == "requests":
        module_description = "Network access ready"
    elif module == "matplotlib.pyplot":
        module_description = "Visualisation ready"
    else:
        module_description = "Module imported successfully"

    try:
        mod = importlib.import_module(module)
        print(f"[OK] {module.split('.')[0]} ({ver_check(module)}) - " +
              module_description)
        return mod
    except ModuleNotFoundError:
        print(f"[FAILURE] - Failed to import module '{module}'")
        return None


if __name__ == "__main__":
    mandatory = ["pandas", "numpy", "matplotlib.pyplot"]
    modules = ["pandas", "numpy", "matplotlib.pyplot", "requests"]
    imported = {}

    for module in modules:
        found = import_checker(module)
        if found:
            imported[module] = found

    if set(mandatory).issubset(imported):
        np = imported["numpy"]
        pd = imported["pandas"]
        mpl = imported["matplotlib.pyplot"]
        rq = imported.get("requests")

        data = np.random.rand(1000)  # type: ignore[attr-defined]
        df = pd.DataFrame(data,  # type: ignore[attr-defined]
                          columns=["value"])

        print(f"Processing {len(df)} data points...")
        print("Generating visualisation...")
        mpl.hist(df["value"], bins=30)  # type: ignore[attr-defined]
        mpl.title("Matrix Data Analysis")  # type: ignore[attr-defined]
        mpl.savefig("heheheh.png")  # type: ignore[attr-defined]
        print("Analysis complete!")
        print("Results saved to: heheheh.png")
    else:
        print("Missing dependencies UwU\nCannot proceed")
