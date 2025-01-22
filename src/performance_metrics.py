import numpy as np

class PerformanceMetrics:
    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)

    @staticmethod
    def max_drawdown(portfolio_values):
        peak = portfolio_values.expanding(min_periods=1).max()
        drawdown = (portfolio_values - peak) / peak
        return drawdown.min()
