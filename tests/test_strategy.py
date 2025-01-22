from src.strategy import Strategy
import pandas as pd

def test_sma_crossover():
    data = pd.DataFrame({"close": [100, 101, 102, 103, 104]})
    strategy = Strategy().sma_crossover(data, short_window=2, long_window=3)
    assert "Signal" in strategy.columns
