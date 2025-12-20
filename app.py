import subprocess
import argparse
import sys
import time

def try_password(archive, password):
    """
    Test a password using 7-Zip without extracting files
    """
    command = [
        "7z", "t",
        archive,
        f"-p{password}",
        "-y"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr

    if "Everything is Ok" in output:
        return True
    return False


def main():
    """
    this tool was writed by Mohammed Hamza Telegram: @lw_w7
    """
    parser = argparse.ArgumentParser(
        description="7-Zip Password Guessing Tool (Educational Use Only)"
    )

    parser.add_argument(
        "-a", "--archive",
        required=True,
        help="Path to the archive file (zip / 7z)"
    )

    parser.add_argument(
        "-w", "--wordlist",
        required=True,
        help="Path to the wordlist file"
    )

    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0.0,
        help="Delay between attempts (seconds)"
    )

    args = parser.parse_args()

    try:
        with open(args.wordlist, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print("[!] Wordlist file not found")
        sys.exit(1)

    print(f"[*] Starting password guessing on: {args.archive}")
    print(f"[*] Total passwords loaded: {len(passwords)}\n")

    start_time = time.time()

    for count, line in enumerate(passwords, start=1):
        password = line.strip()

        if not password:
            continue

        print(f"[-] Trying ({count}): {password}")

        if try_password(args.archive, password):
            elapsed = time.time() - start_time
            print("\n[+] PASSWORD FOUND!")
            print(f"[+] Password: {password}")
            print(f"[+] Time elapsed: {elapsed:.2f} seconds")
            sys.exit(0)

        if args.delay > 0:
            time.sleep(args.delay)

    elapsed = time.time() - start_time
    print("\n[!] Password not found in wordlist")
    print(f"[!] Time elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
