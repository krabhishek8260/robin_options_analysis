# robin_options_analysis

This repository contains a small utility script for exporting your option order history from Robinhood.

## Setup

1. Install dependencies:
   ```bash
   pip install robin-stocks Flask
   ```

## Fetch option orders

Run the script to authenticate and export your option orders to a JSON file.
If you use two-factor authentication, you will be prompted for the code after
entering your password:

```bash
python fetch_options_history.py
```

The script outputs `option_orders.json` containing all option orders associated with the account.

## Web application

Start the Flask web server and visit `http://localhost:5000` in your browser:

```bash
python webapp.py
```

Enter your Robinhood credentials in the form. If 2FA is enabled, provide the
current code as well to download your option orders as JSON. The page is styled
with a simple green theme that resembles Robinhood's login screen.
