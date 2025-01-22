import numpy as np

class PortfolioOptimization:
    @staticmethod
    def optimize_portfolio(expected_returns, covariance_matrix, risk_aversion=1):
        inv_cov_matrix = np.linalg.inv(covariance_matrix)
        weights = inv_cov_matrix.dot(expected_returns) / risk_aversion
        return weights / np.sum(weights)
