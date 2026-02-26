def ft_vault_security():
    classified = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open(classified, "r") as vault_1:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(vault_1.read())
            print()

    except (PermissionError, FileNotFoundError, ZeroDivisionError) as e:
        print("Error:", e)
    try:
        with open("security_protocols.txt", "w") as secure:
            print("SECURE PRESERVATION:")
            new_data = "[CLASSIFIED] New security protocols archived\n"
            secure.write(new_data)
            print(new_data, end="")
            10/0
            print("Vault automatically sealed upon completion\n")
            print("All vault operations completed with maximum security.")

    except (PermissionError, FileNotFoundError, ZeroDivisionError) as e:
        print("Error:", e)


if __name__ == "__main__":
    ft_vault_security()
