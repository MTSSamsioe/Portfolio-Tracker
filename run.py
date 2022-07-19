import gspread
from google.oauth2.service_account import Credentials
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("portfolio_tracker")


def sum_sheet(sheet, range):
    """
    Function that sums up cell range from a google sheet
    """
    sum_tot = 0
    for i in SHEET.worksheet(sheet).get_values(range):

        sum_tot += float(i[0])
    return sum_tot


def validate_char(input_data, allowed_char):
    """
    Function that compares input_data with list of allowed
    characters and returns a list of forbidden characters
    """
    forbidden_char = []
    for char in input_data:
        if char not in allowed_char:
            forbidden_char.append(char)
    return forbidden_char


def nav():
    """
    Function that provides navigation between diffrent sections in the program
    """
    while True:

        print("*" * 60)
        print("\nTo navigate an other section")
        print("type one of the following commands:")
        print("\n" + "*" * 60)
        print("'dash' --> Go to dashboard")
        print("'dash' --> Go to dashboard")
        print("'add' --> Go to add trade section")
        print("'trade' --> Go to trade list section")
        print("'exit' --> Exit program")

        print("\n" + "=" * 50)
        nav_input = input("\nWrite navigation command here : ")
        print("\n" + "=" * 50)
        if nav_input == "dash":
            dashboard()
            break
        elif nav_input == "add":
            update_sheet()
            break
        elif nav_input == "trade":
            trades_list()
            break
        elif nav_input == "exit":
            return False

        else:
            print("\n" + "=" * 50)
            print("\nInvalid command please try again")
            print("\n" + "=" * 50)


# global variables
btc_price = float(SHEET.worksheet("price").get_values("A1")[0][0])
btc_amount = sum_sheet("trades", "D2:D")


def add_date():
    """
    Function that takes input and verifies date format
    before sending data to a Google sheet
    """
    date = []
    print("\n= *")
    print("What date did you buy your bitcoin ? ")
    print("The format has to be DD-MM-2022) ")

    while True:
        try:
            print("\n" + "=" * 50)
            date_input = input("Enter your date here: ")
            print("\n" + "=" * 50)
            datetime.datetime.strptime(date_input, "%d-%m-%Y")
            print(f"\nInput approved the date you entered was {date_input} ")
            date.append(str(date_input))
            break
        except :
            print("\n" + "=" * 50)
            print(ValueError(f"Your date has the wrong format"))
            print(ValueError(f"The date format should be DD-MM-YY"))
            print("Please try again")
            print("\n" + "=" * 50)
    return date


#print(add_date())


def add_amount():
    """
    Function that verifies BTC amount data before sending it to Google sheet
    """
    btc_amount = sum_sheet("trades", "D2:D")
    amount_list = []
    allowed_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-"]
    print("\n" + "=" * 50)
    print("\nWhat amount of BTC did you purchase or sell ?")
    print(
        """\n================================================")
    - Enter a (-)negative amount if you sold BTC
    - Please use a (.) as decimal separator")
    - Alloweed input characters are ('0 - 9', '-', '.')")
    """
    )

    while True:
        print("\n" + "=" * 50)
        amount_input = input("Enter amount here : ")
        print("\n" + "=" * 50)

        check_char = validate_char(amount_input, allowed_char)

        if check_char == [] and len(amount_input) > 0:

            if (float(amount_input) < 0 and (btc_amount + float(amount_input)) > 0) or (
                float(amount_input) > 0 and (btc_amount + float(amount_input)) > 0
            ):

                amount_list.append(str("Bought")) if float(
                    amount_input
                ) > 0 else amount_list.append(str("Sold"))
                print("Input approved...")
                print(f"""New BTC balance is : 
                {(float(amount_input) + btc_amount)}.BTC"""
                )
                amount_list.append(float(amount_input))
                break
            else:

                print(
                    ValueError(
                        f"""Btc sold sold ({amount_input}.BTC) can not be greater than 
                        portfolio balance ({btc_amount}.BTC) 
                        please try again"""
                    )
                )

        else:
            print(
                ValueError(
                    f""" Input empty or Forbidden characters {check_char} 
                    were used please try again"""
                )
            )

    return amount_list


# print(add_amount())


def add_price():
    """
    Function that verifies price data
    before sending it to a Google Spread sheet
    """
    price_list = []
    allowed_char = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    print("\n" + "=" * 50)
    print("\nAt what price did you sell or buy your BTC ?")
    print(
        """\n================================================")
    \n- Please use a (.) as decimal separator")
    \n- Alloweed input characters are ('0 - 9', '.')")
    """
    )

    while True:

        print("\n" + "=" * 50)
        price_input = input("\nEnter price here : ")
        print("\n" + "=" * 50)

        check_char = validate_char(price_input, allowed_char)

        if check_char == [] and len(price_input) > 0:

            print("\n" + "=" * 50)
            print("\nInput approved trade added to trades list")
            price_list.append(float(price_input))

            break

        else:
            print(ValueError(
                    f"""\nInput empty or Forbidden characters {check_char} 
                    were used please try again"""
                )
            )

    return price_list


# print(add_price())

# ========================== MAIN FUNCTIONS=============================


def start():
    """
    Function checks if the portfolio has a name.
    If not you can add one that is then added to the google sheet
    """
    print(
        """
    \n================================================
    \nWelcome to your Bitcoin portfolio tracker
    \n================================================"""
    )
    if SHEET.worksheet("name").get_values() == []:

        print("Please pick a name for your portfolio")
        print("\n" + "=" * 50)
        portfolio_name_input = [input("Please enter your portfolio name:")]
        print("\n" + "=" * 50)
        SHEET.worksheet("name").append_row(portfolio_name_input)
    else:
        portfolio_name = SHEET.worksheet("name").get_values()

        print(f"\nYour portfolio {str(portfolio_name[0][0])} Is now loaded !")
        print("\n" + "=" * 50)


#start()


def dashboard():
    """
    Function that shows dashboard with
    current value of portfolio, profit/loss etc
    """
    
    btc_amount = sum_sheet("trades", "D2:D")
    btc_value = round(btc_amount * btc_price, 2)
    avg_len_never_0 = 1 if len(SHEET.worksheet("trades").get_values("E2:E")) == 0 \
            else len(SHEET.worksheet("trades").get_values("E2:E"))
    avg_buy_price = round(
        sum_sheet("trades", "E2:E") / avg_len_never_0 ,
        2
    )
    avg_buy_price_value = round(avg_buy_price * btc_amount, 2)
    
    avg_buy_price_value_never_0 = 1 if avg_buy_price_value <= 0 else avg_buy_price_value


    percent_profit_or_loss = (
        0 if btc_amount <= 0 else
        (btc_value - avg_buy_price_value_never_0) / btc_value * 100
    )
    ternary_plus_minus_percent = (
         +round(percent_profit_or_loss, 2)
        if avg_buy_price_value_never_0 < btc_value
        else round(percent_profit_or_loss * -1, 2)
    )
    print(avg_buy_price_value_never_0)
    print(btc_value)
    print(percent_profit_or_loss)
    print(ternary_plus_minus_percent)
    print(
        """
    \n================================================
    \n*** BITCOIN PORTFOLIO TRACKER - DASHBOARD ***
    \n================================================
    """
    )
    print(f"\nYour BTC balance is: {btc_amount} BTC")
    print("\n" + "=" * 50)
    print(f"\nCurrrent BTC value in USD$ is : {btc_value} $")
    print("\n" + "=" * 50)
    print(f"\nYour average BTC buy price in USD$ is : {avg_buy_price} $")
    print("\n" + "=" * 50)
    print(f"\nYour BTC value on average buy price is : {avg_buy_price_value} $")
    print("\n" + "=" * 50)
    print(f"\nAverage pofit and loss is: {ternary_plus_minus_percent} %")
    print("\n" + "=" * 50)
    nav()



dashboard()


def update_sheet():
    list = []
    length = len(SHEET.worksheet("trades").get_values("A2:A"))
    list.append(length + 1)
    list.append(add_date()[0])
    two_values_list = add_amount()
    type, amount = two_values_list
    list.append(type)
    list.append(amount)
    list.append(add_price()[0])
    SHEET.worksheet("trades").append_row(list)
    nav()


# update_sheet()


def trades_list():
    """
    Function that creates class instances of trades that has been made.
    """

    class Trade:
        def __init__(self, number, date, type, amount, price):
            self.number = number
            self.date = date
            self.type = type
            self.amount = amount
            self.price = price

        def __str__(self):
            return (
                "\nTrade number; "
                + self.number
                + "\nTrade date: "
                + self.date
                + "\nTrade type: "
                + self.type
                + "\nBTC amount: "
                + self.amount
                + "\nBTC price: "
                + self.price
            )

    values_data = SHEET.worksheet("trades").get_values("A2:E")

    print(
        """
    \n================================================
    \n*** BITCOIN PORTFOLIO TRACKER - TRADES LIST ***
    \n================================================"""
    )
    print("\nBelow is a list of all your trades")
    for i in range(len(values_data)):
        if len(values_data) > 0:
            tradei = Trade(
                values_data[i][0],
                values_data[i][1],
                values_data[i][2],
                values_data[i][3],
                values_data[i][4],
            )
            print("\n" + "=" * 50)
            print(tradei)
        else:
            print("\n" + "=" * 50)
            print("There are no trades in the list please add trades first")
            print("\n" + "=" * 50)
    nav()


#nav()
