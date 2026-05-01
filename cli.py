from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging
from colorama import Fore, Style, init

init(autoreset=True)


def menu():
    print(Fore.CYAN + "\n==============================")
    print(Fore.YELLOW + "      TRADING BOT MENU")
    print(Fore.CYAN + "==============================")
    print(Fore.GREEN + "1. Place MARKET Order")
    print(Fore.GREEN + "2. Place LIMIT Order")
    print(Fore.RED + "3. Exit")
    print(Fore.CYAN + "==============================\n")
def run_order(order_type):
    print(Fore.CYAN + "\n==============================")
    print(Fore.YELLOW + f"   {order_type} ORDER MODE")
    print(Fore.CYAN + "==============================\n")

    symbol = input(Fore.YELLOW + "Symbol (e.g. BTCUSDT): ")

    try:
        client = BinanceClient()

        
        try:
            price_now = client.get_price(symbol)
            print(Fore.BLUE + f"\n Current Price: {price_now}\n")
        except:
            print(Fore.RED + " Could not fetch live price\n")

        side = input(Fore.YELLOW + "Side (BUY/SELL): ")
        quantity = float(input(Fore.YELLOW + "Quantity: "))

        price = None
        if order_type == "LIMIT":
            price = float(input(Fore.YELLOW + "Price: "))

        validate_inputs(symbol, side, order_type, quantity, price)

        print(Fore.BLUE + "\nPlacing order...\n")

        order = place_order(
            client.get_client(),
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print(Fore.CYAN + "\n==============================")
        print(Fore.GREEN + " ORDER RESULT")
        print(Fore.CYAN + "==============================")

        print(Fore.WHITE + str(order))

        if order.get("orderId"):
            print(Fore.GREEN + "\n Order placed successfully")
            print(Fore.BLUE + f"Status: {order.get('status')}")
        else:
            print(Fore.RED + "\n✘ Order failed")

    except Exception as e:
        print(Fore.RED + f"\nError: {e}")
def main():
    setup_logging()

    while True:
        menu()
        choice = input("Choose option: ")

        try:
            if choice == "1":
                run_order("MARKET")

            elif choice == "2":
                run_order("LIMIT")

            elif choice == "3":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()