# pip install mplfinance
import pandas as pd
import mplfinance as mpf

dates = pd.date_range("2026-08-17", periods=5, freq="D")
df = pd.DataFrame(
    {
        "Open":  [100, 103, 101, 105, 108],
        "High":  [104, 105, 106, 109, 110],
        "Low":   [99, 100, 100, 104, 106],
        "Close": [103, 101, 105, 108, 107],
    },
    index=dates,
)
df.index.name = "Date"

mpf.plot(df, type="candle", title="5-day OHLC")
