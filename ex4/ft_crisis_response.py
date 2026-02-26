print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

try:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    with open("lost_archive.txt", "r") as lost:
        print(lost.read())
except (FileNotFoundError, PermissionError):
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

print()

try:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    with open("classified_data.txt", "r") as vault:
        print(vault.read())
except (PermissionError, FileNotFoundError):
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

print()

try:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    with open("standard_archive.txt", "r") as standard:
        print(f"SUCCESS: Archive recovered - {standard.read()}")
        print("STATUS: Normal operations resumed")
        print("\nAll crisis scenarios handled successfully. Archives secure.")

except (FileNotFoundError, PermissionError, IsADirectoryError) as e:
    print(f"Erro: {e}")
