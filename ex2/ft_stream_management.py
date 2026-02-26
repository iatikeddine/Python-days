import sys


def ft_stream_management():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")

    print()
    print(
        f"[STANDARD] Archive status from {archivist_id}: "
        f"{status_report}"
    )
    print(
        "[ALERT] System diagnostic: "
        "Communication channels verified", file=sys.stderr
    )
    print("[STANDARD] Data transmission complete")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
