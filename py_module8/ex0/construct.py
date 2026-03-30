import sys
import os
import site


def outside_env() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    # grabs python executable current path
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    # instructions showing how to create a virtual environement
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\nScripts\nactivate # On Windows\n")
    print("Then run this program again.")


def inside_env() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    # Extract virtual environement name from the path
    venv_name = os.path.basename(sys.prefix)
    print(f"Virtual Environment: {venv_name}")
    # Shows the environement path
    env_path = sys.prefix
    print(f"Environment Path: {env_path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    # Extract the primary package name
    site_packages = site.getsitepackages()[0]
    print(f"Package installation path: {site_packages}")


if __name__ == "__main__":
    try:
        # if current python executable path matches the global python path
        # that means we are currently outside the virtual environement
        if sys.prefix == sys.base_prefix:
            outside_env()
        else:
            inside_env()
    except Exception as e:
        print(e)
