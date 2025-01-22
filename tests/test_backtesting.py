from src.backtesting import Backtester
from src.market_simulator import MarketSimulator
from src.strategy import Strategy
import pandas as pd

def test_backtesting():
    data = pd.DataFrame({"close": [100, 101, 102, 103, 104]})
    simulator = MarketSimulator(historical_data=data)
    strategy = Strategy().sma_crossover
    backtester = Backtester(strategy, simulator)
    result = backtester.run(data)
    assert result > 0
