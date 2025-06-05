import json
import getpass
import robin_stocks.robinhood as r


def login():
    """Prompt for credentials and perform Robinhood login."""
    username = input("Robinhood username: ")
    password = getpass.getpass("Robinhood password: ")
    mfa = input("2FA code (if enabled, otherwise leave blank): ")
    r.login(username=username, password=password, mfa_code=mfa or None)


def fetch_all_option_orders() -> list:
    return r.orders.get_all_option_orders()


def main():
    login()
    orders = fetch_all_option_orders()
    with open("option_orders.json", "w") as f:
        json.dump(orders, f, indent=2)
    print(f"Saved {len(orders)} orders to option_orders.json")


if __name__ == "__main__":
    main()
