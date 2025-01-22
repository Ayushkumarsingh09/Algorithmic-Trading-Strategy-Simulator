import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_equity_curve(dates, portfolio_values):
        plt.figure(figsize=(12, 6))
        plt.plot(dates, portfolio_values, label="Equity Curve")
        plt.title("Equity Curve")
        plt.xlabel("Date")
        plt.ylabel("Portfolio Value")
        plt.legend()
        plt.grid()
        plt.show()
