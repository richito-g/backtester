from engine.portfolio import Portfolio
from engine.strategy import BaseStrategy
from engine.candle import Candle

def run_backtest(
    candles: list[Candle],
    strategy: BaseStrategy,
    initial_cash: float,
    profit_perc: float,
    stop_loss_perc: float,
    fraction_of_cash: float
) -> Portfolio:

  portfolio = Portfolio(initial_cash)

  for candle in candles:
    if strategy.should_enter(candle) and not portfolio.has_open_position():
      portfolio.enter_trade(
          candle,
          profit_perc=profit_perc,
          stop_loss_perc=stop_loss_perc,
          fraction_of_cash=fraction_of_cash
      )

    portfolio.update_on_candle(candle)

  return portfolio