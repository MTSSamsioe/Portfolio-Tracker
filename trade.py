class Trade:
    def __init__(self, number, date, trade_type, amount, price):
        self.number = number
        self.date = date
        self.trade_type = trade_type
        self.amount = amount
        self.price = price
        """ code below imitated from youtube video
        https://www.youtube.com/watch?v=9ciQeqyuiek&t=187s
        by Eybar Vasquez Nevarez
        """

    def __str__(self):
        """Method prints the trade instance created"""
        return (
            "\nTrade number; " +
            self.number +
            "\nTrade date: " +
            self.date +
            "\nTrade type: " +
            self.trade_type +
            "\nBTC amount: " +
            self.amount +
            "\nBTC price: " +
            self.price
        )
