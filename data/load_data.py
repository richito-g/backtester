import yfinance as yf
import pandas as pd
from engine.candle import Candle

def load_price_data(
    ticker: str = "BTC-USD",
    start: str = "2020-01-01",
    end: str = None
) ->list[Candle]:
  
  df = yf.download(ticker, start=start, end=end)
  df = df.dropna()
  
  if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)
  candles: list[Candle] = []

  for idx, row in enumerate(df.itertuples()):
    candles.append(
      Candle(
        open = float(row.Open),
        high = float(row.High),
        low = float(row.Low),
        close = float(row.Close),
        index = idx
      )
    )
  return candles