import pandas as pd

class Strategy:
    def sma_crossover(self, data, short_window=50, long_window=200):
        data["SMA_Short"] = data["close"].rolling(window=short_window).mean()
        data["SMA_Long"] = data["close"].rolling(window=long_window).mean()
        data["Signal"] = 0
        data.loc[data["SMA_Short"] > data["SMA_Long"], "Signal"] = 1
        data.loc[data["SMA_Short"] <= data["SMA_Long"], "Signal"] = -1
        return data

    def rsi_strategy(self, data, rsi_period=14, overbought=70, oversold=30):
        delta = data["close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=rsi_period).mean()
        avg_loss = loss.rolling(window=rsi_period).mean()
        rs = avg_gain / avg_loss
        data["RSI"] = 100 - (100 / (1 + rs))

        data["Signal"] = 0
        data.loc[data["RSI"] > overbought, "Signal"] = -1
        data.loc[data["RSI"] < oversold, "Signal"] = 1
        return data
