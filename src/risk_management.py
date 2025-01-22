class RiskManagement:
    @staticmethod
    def position_sizing(capital, risk_per_trade, stop_loss_pct):
        return (capital * risk_per_trade) / stop_loss_pct

