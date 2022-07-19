class trade:
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