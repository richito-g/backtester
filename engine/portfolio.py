from engine.trade import Trade
from engine.candle import Candle

class Portfolio:
  def __init__(self, initial_cash: float):
    self.initial_cash = float(initial_cash)
    self.cash = float(initial_cash)

    self.open_trade: Trade | None = None
    self.closed_trades: list[Trade] = []

    self.equity_curve: list[tuple[int, float]] = []

  def has_open_position(self) -> bool:
    return self.open_trade is not None and not self.open_trade.is_closed

  def enter_trade(self, candle: Candle, profit_perc: float, stop_loss_perc: float) ->bool:
    if self.has_open_position():
      return False

    buy_price = candle.open
    if buy_price > self.cash:
      return False

    self.cash -= buy_price

    self.open_trade = Trade(
        buy_price = buy_price,
        buy_index = candle.index,
        profit_perc = profit_perc,
        stop_loss_perc = stop_loss_perc
    )

    return True

  def update_on_candle(self, candle: Candle)->None:
    if self.open_trade is not None and not self.open_trade.is_closed:
      closed_now = self.open_trade.try_to_close(candle)
      if closed_now:
        self.cash += self.open_trade.sell_price
        self.closed_trades.append(self.open_trade)
        self.open_trade = None

    self.equity_curve.append((candle.index, self.equity(candle)))

  def equity(self, candle:Candle) ->float:
    eq =self.cash
    if self.open_trade is not None and not self.open_trade.is_closed:
      eq += candle.close
    return eq