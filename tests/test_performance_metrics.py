from src.performance_metrics import PerformanceMetrics
import pandas as pd

def test_performance_metrics():
    returns = pd.Series([0.01, -0.02, 0.03, -0.01])
    sharpe_ratio = PerformanceMetrics.calculate_sharpe_ratio(returns)
    assert sharpe_ratio != 0
