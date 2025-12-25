import matplotlib.pyplot as plt
from engine.portfolio import Portfolio

def plot_equity_curve(portfolio: Portfolio):
  xs = [i for i, eq in portfolio.equity_curve]
  ys = [eq for i, eq in portfolio.equity_curve]

  plt.figure()
  plt.plot(xs,ys)
  plt.title("Equity Curve")
  plt.xlabel("Candle Index")
  plt.ylabel("Equity")
  plt.show()
