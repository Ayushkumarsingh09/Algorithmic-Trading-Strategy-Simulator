import os
import numpy as np

class BacktestReport:
    @staticmethod
    def generate_report(data, starting_cash, output_path="outputs/reports/backtest_summary.txt"):
        # Performance metrics
        total_return = (data['Portfolio Value'].iloc[-1] - starting_cash) / starting_cash
        annualized_return = (1 + total_return) ** (252 / len(data)) - 1
        data['Daily Return'] = data['Portfolio Value'].pct_change()
        sharpe_ratio = np.mean(data['Daily Return']) / np.std(data['Daily Return']) * np.sqrt(252)
        max_drawdown = (data['Portfolio Value'] / data['Portfolio Value'].cummax() - 1).min()

        # Generate summary report
        summary = f"""
        Backtest Summary Report
        ------------------------
        Total Return: {total_return:.2%}
        Annualized Return: {annualized_return:.2%}
        Sharpe Ratio: {sharpe_ratio:.2f}
        Max Drawdown: {max_drawdown:.2%}
        Starting Cash: ${starting_cash:,.2f}
        Ending Portfolio Value: ${data['Portfolio Value'].iloc[-1]:,.2f}
        """

        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write to file
        with open(output_path, "w") as file:
            file.write(summary)

        print(f"Backtest summary saved to {output_path}")
