def ft_vault_security():
    classified = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        with open(classified, "r") as vault_1:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(vault_1.read())

        try:
            with open("security_protocols.txt", "r") as secure:
                print("\nSECURE PRESERVATION:")
                print(secure.read())
                print("Vault automatically sealed upon completion")
                print("\nAll vault operations completed with maximum security.")
        except (PermissionError, FileNotFoundError) as e:
            print("Error:", e)
    except (PermissionError, FileNotFoundError) as e:
        print("Error:", e)