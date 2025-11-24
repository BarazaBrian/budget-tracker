# Budget Tracker

Overview
--------
This is a simple command-line Budget Tracker written in Python 3. It lets you add income and expenses, list and filter transactions, and view summaries within a single terminal session. All data is stored in memory for the duration of the session (no file I/O).

Files
-----
- tracker.py — Contains Transaction, Income, Expense, and BudgetTracker classes.
- main.py — Command-line interface and main program loop.

Features
----------------------------------------
- Add transactions: date, amount, category, description, and type (income/expense).
- List transactions in a readable table.
- Filter transactions by type, category, or month (YYYY-MM).
- Summary: total income, total expenses, balance, and per-category totals.
- Input validation: enforces date format, numeric positive amounts, valid menu choices.
- Session-only: no saving or loading to files — data remains in memory.

Running
-------
Requirements: Python 3.8+ (should work on Python 3.6+).

From PowerShell in the project root run:


python .\main.py


Menu
----
1) Add income
2) Add expense
3) List transactions
4) Filter (by category / type / month)
5) Show summary
6) Undo last transaction (optional)
0) Exit

Sample interaction
---------------------------
Add Income

![Add Income](https://i.imgur.com/XpRL3Rg.jpeg)

Add Expense

![Add Expense](https://i.imgur.com/RIXjviW.jpeg)

List Transactions

![List Transactions](https://i.imgur.com/ndeoLZV.jpeg)

Filter Transactions

![Filter Transactions](https://i.imgur.com/JccImp0.jpeg)

Show Summary

![Show Summary](https://i.imgur.com/LSBIJwZ.jpeg)

Notes
--------------------------
- What I learned: basic OOP in Python, building a user-friendly CLI, and careful input validation.
- Challenges: parsing and validating user input robustly, and making concise CLI output that stays readable.
- Future improvements: add file persistence (CSV/JSON), nicer table formatting, unit tests and undo stack.

Author
--------------------------
[Baraza Mwololo Brian](https://github.com/BarazaBrian)