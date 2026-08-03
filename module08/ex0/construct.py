import sys
import site

if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        print(f"""
MATRIX STATUS: You're still plugged in

Current Python: {sys.executable}
Virtual environment: None detected

WARNING: You're in the global environment

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows

Then run this program again
""")
    else:
        print(f"""
MATRIX STATUS: Welcome to the construct

Current Python: {sys.executable}
Virtual environment: {sys.prefix.split('/')[-1]}
Environment Path: {sys.prefix}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.

Package installation path:
{site.getsitepackages()[0]}
""")
