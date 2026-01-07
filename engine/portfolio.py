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

  def enter_trade(self, candle: Candle, profit_perc: float, stop_loss_perc: float, fraction_of_cash: float, fee_rate = 0.0) ->bool:
    if fraction_of_cash<=0 or fraction_of_cash >1:
      return False
    if self.has_open_position():
      return False

    buy_price = candle.open
    spend = self.cash*fraction_of_cash
    qty = spend/buy_price
    
    trade = Trade(
      buy_price=buy_price,
      buy_index=candle.index,
      qty=qty,
      profit_perc=profit_perc,
      stop_loss_perc=stop_loss_perc,
      fee_rate=fee_rate
    )

    cost = buy_price*qty
    total_debt = cost + trade.buy_fee

    if total_debt > self.cash:
      return False

    self.cash -= total_debt
    self.open_trade = trade
    return True

  def update_on_candle(self, candle: Candle)->None:
    if self.open_trade is not None and not self.open_trade.is_closed:
      closed_now = self.open_trade.try_to_close(candle)
      if closed_now:
        proceeds = self.open_trade.qty * self.open_trade.sell_price
        self.cash += proceeds - self.open_trade.sell_fee
        self.closed_trades.append(self.open_trade)
        self.open_trade = None

    self.equity_curve.append((candle.index, self.equity(candle)))

  def equity(self, candle:Candle) ->float:
    eq =self.cash
    if self.open_trade is not None and not self.open_trade.is_closed:
      eq += self.open_trade.qty*candle.close
    return eq