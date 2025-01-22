import pytest
from src.market_simulator import MarketSimulator

def test_market_simulator():
    data = {"close": [100, 102, 101, 103]}
    simulator = MarketSimulator(historical_data=data)

    simulator.execute_order("2024-01-01", "buy", 10, 100)
    assert simulator.position == 10
    assert simulator.cash == 100000 - 1000

    simulator.execute_order("2024-01-02", "sell", 5, 102)
    assert simulator.position == 5
    assert simulator.cash == 100000 - 1000 + (5 * 102)
