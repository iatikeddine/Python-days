import sys


total = len(sys.argv)
print("=== Command Quest ===")
if total < 2:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {total - 1}")
    i = 1
    while i < total:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1

print(f"Total arguments: {total}")