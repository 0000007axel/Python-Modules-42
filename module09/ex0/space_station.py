try:
    from pydantic import BaseModel
except ModuleNotFoundError:
    print("""
Could not import the pydantic module

Try 'pip install pydantic'
""")
