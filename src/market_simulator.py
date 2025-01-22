import numpy as np
import pandas as pd

class MarketSimulator:
    def __init__(self, historical_data, starting_capital=100000):
        self.data = historical_data
        self.capital = starting_capital
        self.position = 0
        self.cash = starting_capital
        self.portfolio_value = starting_capital

    def execute_order(self, date, order_type, quantity, price):
        if order_type == "buy":
            cost = quantity * price
            if self.cash >= cost:
                self.cash -= cost
                self.position += quantity
                print(f"Bought {quantity} units at {price} on {date}")
            else:
                print("Insufficient cash to execute buy order")
        elif order_type == "sell":
            if self.position >= quantity:
                revenue = quantity * price
                self.cash += revenue
                self.position -= quantity
                print(f"Sold {quantity} units at {price} on {date}")
            else:
                print("Insufficient position to execute sell order")

    def calculate_portfolio_value(self, current_price):
        self.portfolio_value = self.cash + self.position * current_price
        return self.portfolio_value
