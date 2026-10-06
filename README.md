# dr_python

A simple CLI mockup of a doctor's record-keeping system: sign up, sign in, and log patient visits (prescription, date, fee) to a CSV file.

## Setup

The program reads from and writes to two CSV files, `database.csv` (user accounts) and `patients.csv` (patient records). These are not included in the repo, so before running the program you need to create them yourself in the project root with the following headers:

**database.csv**
```
name,number,mail
```

**patients.csv**
```
name,prescription,date,fee
```

## Usage

```
python dr_python.py
```

You'll be prompted to `Sign_in`, `Sign_up`, or `Exit`:

- **Sign_up** — register with a name, number, and mail; saved to `database.csv`.
- **Sign_in** — enter your number to look yourself up in `database.csv`.
- After signing in/up, enter patient records (name, prescription, date, fee) one at a time, saved to `patients.csv`. Enter `N` as the patient name to exit.

## Credits

Code written by me. Claude Code helped with commenting and basic syntax error identification.
