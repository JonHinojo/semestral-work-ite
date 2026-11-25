# Password Strength Checker

A small Python program that checks if a password is Weak, Medium or Strong,
and explains why. It can be used from the terminal or from a simple web page.

Example: "Summer2024" gives "Medium: shorter than 12 characters and no symbols".

## How it works

First, the program checks some filters:
- If the password is empty or only has spaces, it shows an error and asks again.
- If it has less than 8 characters, it is Weak.
- If it is in a list of common passwords, it is Weak.

If the password passes the filters, it gets points:
- Length: 1 point for 8 to 11 characters, 2 points for 12 or more.
- Character types: 1 point for each type it has (lowercase, uppercase, digits and symbols).

The maximum is 6 points. From 0 to 2 it is Weak, from 3 to 4 it is Medium, and from 5 to 6 it is Strong.
Every time a rule does not give all its points, the program says what is missing.

The full flow is shown in this UML activity diagram:

docs/diagrams/activity_diagram.drawio

More details about the design are in docs/notes.md.

## Project structure

- main.py: terminal version
- app.py: web version with Flask
- src/password_checker.py: all the logic (one function for each rule)
- templates/ and static/: the HTML page and its CSS
- data/common_passwords.txt: list of common passwords
- tests/: unit tests
- test_main.py: runs all the tests
- docs/: design notes, test plan and diagram

## Installation

You need Python 3 installed.

```
git clone https://github.com/JonHinojo/semestral-work-ite.git
cd semestral-work-ite
pip install -r requirements.txt
```

The only external library is Flask, and it is only needed for the web version.

## Usage

Terminal version:

```
python main.py
```

Web version:

```
python app.py
```

Then open http://127.0.0.1:5000 in the browser. To stop the server, press Ctrl+C in the terminal.

## Tests

The tests are written with unittest. To run all of them:

```
python test_main.py
```

The test plan, with the reasons for each test case, is in docs/tests.md.

## Limitations

- Only the 32 basic keyboard symbols count as symbols. Characters like €, ¿ or ¡ do not give the symbol point.
- The common password check only finds exact matches. For example, "password" is detected, but "password123!" may not be.
- The program does not detect patterns like "123" or "qwerty" inside a longer password.
- If the file data/common_passwords.txt is deleted, the program stops with an error.
- The common password file is read every time a password is checked. This is fine for one password, but it would be slow for many.
- The web version uses the Flask development server, so it is only for local use, not for a real website.

## Credits

The list of common passwords in data/common_passwords.txt comes from the
SecLists project by Daniel Miessler. I used the file
Passwords/Common-Credentials/10k-most-common.txt, which has the 10,000 most
common passwords found in real data leaks.

- Repository: https://github.com/danielmiessler/SecLists
- License: MIT

## License

This project is under the MIT License. See the LICENSE file.