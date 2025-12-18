======================
# 7-ZIP PASSWORD GUESSING TOOL (PYTHON) #
======================

Author  : Mohammed Hamza
Telegram: @lw_w7
Instagram: @lw__w6
TikTok  : @pr_mh

======================
DISCLAIMER
======================

This tool is created for EDUCATIONAL and AUTHORIZED USE ONLY.

You are allowed to use this tool ONLY on:
- Your own archives
- Archives you have explicit permission to test

Any illegal or unauthorized use of this tool is strictly forbidden.
The author is NOT responsible for any misuse.

======================
ABOUT THE TOOL
======================

This is a Python-based password guessing tool that integrates
with the 7-Zip command-line utility.

The tool tests passwords against encrypted ZIP or 7Z archives
using a wordlist, WITHOUT extracting the files.

It is designed for:
- Cybersecurity education
- Understanding password protection
- Demonstrating brute-force concepts
- Teaching Python + system tools integration

======================
FEATURES
======================

✔ Uses 7-Zip (AES supported)
✔ Supports ZIP and 7Z archives
✔ Wordlist-based password guessing
✔ Uses argparse for professional CLI usage
✔ Detects correct password by parsing 7-Zip output
✔ Optional delay between attempts
✔ Clean and readable output
✔ Educational and beginner-friendly code

======================
REQUIREMENTS
======================

- Python 3.x
- 7-Zip installed
- 7z added to system PATH
- Windows / Linux / macOS (with 7z)

======================
INSTALLATION
======================

1. Install Python:
   https://www.python.org/

2. Install 7-Zip:
   https://www.7-zip.org/

3. Verify 7-Zip installation:
   Open terminal / CMD and run:
   7z

======================
USAGE
======================

Basic usage:
------------------------------------------------------------
python zip_bruteforce.py -a secure.zip -w wordlist.txt

With delay between attempts:
------------------------------------------------------------
python zip_bruteforce.py -a secure.zip -w wordlist.txt -d 0.2

Arguments:
------------------------------------------------------------
-a, --archive   Path to the archive file (ZIP / 7Z)
-w, --wordlist  Path to the wordlist file
-d, --delay     Delay between attempts (seconds)

======================
HOW IT WORKS
======================

- Reads passwords from a wordlist
- Uses 7-Zip "test" mode (7z t)
- Tries each password without extracting files
- Parses output for "Everything is Ok"
- Stops immediately when the correct password is found

======================
LIMITATIONS
======================

- This tool does NOT use GPU
- Much slower than professional tools like Hashcat
- Depends heavily on wordlist quality
- Intended for learning, not real-world attacks

======================
EDUCATIONAL VALUE
======================

This project demonstrates:
- Python subprocess usage
- CLI tool development with argparse
- External tool integration
- Security awareness concepts
- Difference between ZIP and 7Z encryption
- Why strong passwords matter

======================
LICENSE
======================

This project is released for educational use.
Redistribution is allowed WITH proper credit to the author.

======================
AUTHOR
======================

Mohammed Hamza
Cybersecurity & Programming Educator

Telegram : @lw_w7
Instagram: @lw__w6
TikTok   : @pr_mh

============================================================
