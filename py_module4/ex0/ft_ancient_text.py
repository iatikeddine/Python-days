def ft_ancient_text() -> None:
    vault = "ancient_fragment.txt"
    file = None

    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print(f"Accessing Storage Vault: {vault}")
        file = open(vault, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if file:
            file.close()
            print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
