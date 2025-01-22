from src.visualization import Visualization
import pandas as pd

def test_plot_equity_curve():
    dates = pd.date_range(start="2024-01-01", periods=10)
    portfolio_values = [100000 + i * 1000 for i in range(10)]
    Visualization.plot_equity_curve(dates, portfolio_values)
