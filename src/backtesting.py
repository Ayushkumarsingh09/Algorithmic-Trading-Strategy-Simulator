import pandas as pd

class Backtester:
    def __init__(self, strategy, simulator):
        self.strategy = strategy
        self.simulator = simulator

    def run(self, data):
        strategy_data = self.strategy(data)
        for date, row in strategy_data.iterrows():
            if row["Signal"] == 1:  # Buy signal
                self.simulator.execute_order(date, "buy", 10, row["close"])
            elif row["Signal"] == -1:  # Sell signal
                self.simulator.execute_order(date, "sell", 10, row["close"])
        return self.simulator.calculate_portfolio_value(strategy_data.iloc[-1]["close"])
