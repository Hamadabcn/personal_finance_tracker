# Personal Finance Tracker

This project is a simple personal finance tracker to help you manage your income and expenses. It allows you to add transactions, view transactions within a date range, and visualize your financial data using plots.

## Features

- Add new transactions with date, amount, category (Income or Expense), and description.
- View transactions within a specified date range.
- Summary of total income, total expenses, and net savings.
- Plot income and expenses over time.

## Requirements

- Python 3.x
- Required Python packages:
  - `pandas`
  - `matplotlib`

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Hamadabcn/personal_finance_tracker.git
   
Navigate to the project directory:
cd personal_finance_tracker

Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux


Install the required packages:
pip install pandas matplotlib

Run the main script:
python py.main.py

Project Structure:
personal_finance_tracker/
│
├── py.main.py                  # Main script to run the application
├── data_entry.py               # Helper functions for user input
├── finance_data.csv            # CSV file to store transaction data (created on first run)
└── README.md                   # Project documentation

