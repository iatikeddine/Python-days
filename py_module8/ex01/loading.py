def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    ready = True
    # Try to load pandas
    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except Exception:
        print("[FAIL] pandas is missing. Data manipulation unavailable.")
        ready = False
    
    # Try to load numpy
    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except Exception as e:
        print("[FAIL] numpy is missing. Numerical computation unavailable.")
        ready = False

    # Try to load matplotlib
    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ImportError:
        print("[FAIL] matplotlib is missing. Visualization unavailable.")
        ready = False

    # Try to load requests
    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("[FAIL] requests is missing. Network access unavailable.")
        ready = False
    return ready

def analyze_data() -> None:
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        # Pandas Data Manipulation
        data = {'Name': ['Karim', 'Lora', 'kemmich', 'Sophia'],
                'Height': [175, 160.5, 189, 170.3],
                'Age': [17, 22, 24, 19],
                "Nationality": ['Morocco', 'France', 'Germany', 'Spain']}
        
        df = pd.DataFrame(data)
        print("\n--- Raw DataFrame ---")
        print(df)
        print("\n")

        # Numpy computation
        ages = df["Age"]
        heights = df["Height"]
        average_age = np.mean(ages)
        average_height = np.mean(heights)
        print("--- Numpy Computations ---")
        print(f"Average Age: {average_age:.1f} years")
        print(f"Average height: {average_height:.1f} cm")

        # Matplotlib visualization
        print("\nGenerating visualization...")
        # creating a chart with Names in X and Heights in Y 
        plt.bar(df["Name"], df["Height"], color=["blue"])
        plt.title("Height Analysis")
        plt.xlabel("Name")
        plt.ylabel("Height (cm)")
        # Save the result in png file
        filename = "matrix_analysis.png"
        plt.savefig(filename)
        plt.close()
        print("Analysis complete!")
        print(f"Results saved to: {filename}")

    except Exception as e:
        print(e)

def test_network() -> None:
    print("\nTesting external network connection...")
    try:
        import requests
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("Connection to the outside world established.")
    except Exception as e:
        print("Network offline")

def demonstrate_managers() -> None:
    print("\n--- Package Manager Difference---")
    try:
        import pandas as pd
        
        # Grab the absolute path where pandas was installed
        install_path = pd.__file__.lower()
        
        if "poetry" in install_path:
            print("[ACTIVE] POETRY Environment Detected")
        else:
            print("[ACTIVE] PIP Environment Detected")
            
    except ImportError:
        print("Install dependencies to see the environment context.")


if __name__ == "__main__":
    if check_dependencies():
        analyze_data()
        test_network()
        demonstrate_managers()