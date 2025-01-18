from src.risk_management import RiskManagement

def test_position_sizing():
    capital = 100000
    risk_per_trade = 0.01
    stop_loss_pct = 0.02
    size = RiskManagement.position_sizing(capital, risk_per_trade, stop_loss_pct)
    assert size == 500
