from engine.portfolio import Portfolio
from engine.candle import Candle
from engine.stats import Stats


def compute_stats(portfolio: Portfolio, candles: list[Candle]) -> Stats:
  trades = portfolio.closed_trades
  num_trades = len(trades)

  total_profit = sum(getattr(t, "profit", 0.0) for t in trades)
  num_wins = sum(1 for t in trades if getattr(t, "profit", 0.0) > 0)
  num_losses = sum(1 for t in trades if getattr(t, "profit", 0.0) <= 0)

  win_rate =(num_wins/num_trades) if num_trades > 0 else 0.0

  final_equity = portfolio.equity_curve[-1][1] if portfolio.equity_curve else portfolio.cash
  perc_return = (final_equity/portfolio.initial_cash - 1.0)

  first_open = candles[0].open
  last_close = candles[-1].close
  perc_return_buy_and_hold = (last_close/first_open - 1.0)

  equities = [eq for _, eq in portfolio.equity_curve]
  max_dd, max_dd_abs = compute_max_drawdown(equities)

  return Stats(
      num_trades=num_trades,
      win_rate=win_rate,
      num_wins=num_wins,
      num_losses=num_losses,
      perc_return=perc_return,
      perc_return_buy_and_hold = perc_return_buy_and_hold,
      initial_cash=portfolio.initial_cash,
      total_profit=total_profit,
      max_drawdown=max_dd,
      max_drawdown_abs=max_dd_abs
  )

def compute_max_drawdown(equities: list[float]) ->tuple[float, float]:
  if not equities:
    return 0.0, 0.0
  
  peak = equities[0]
  max_dd = 0.0
  max_dd_abs = 0.0

  for eq in equities:
      if eq>peak:
        peak = eq

      dd = (eq/peak) - 1.0
      dd_abs = peak - eq

      if dd<max_dd:
        max_dd = dd
      if dd_abs >max_dd_abs:
        max_dd_abs = dd_abs

  return max_dd, max_dd_abs