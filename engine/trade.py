from engine.candle import Candle

class Trade:
    def __init__(self, buy_price, buy_index, profit_perc, stop_loss_perc):
      self.buy_price = buy_price
      self.buy_index = buy_index

      self.profit_perc = profit_perc
      self.stop_loss_perc = stop_loss_perc

      self.sell_price = None
      self.sell_index = None
      self.is_closed = False
      self.take_profit_val = None
      self.stop_loss_val = None

      self.update()

    def update(self, curr_candle = None):
      self.take_profit_val = self.buy_price * (1+self.profit_perc)
      self.stop_loss_val = self.buy_price * (1 - self.stop_loss_perc)

    def try_to_close(self, curr_candle):
      if self.is_closed:
        return False
      if curr_candle.low <=self.stop_loss_val:
        self.close_trade(self.stop_loss_val, curr_candle.index)
        return True
      elif curr_candle.high >= self.take_profit_val:
        self.close_trade(self.take_profit_val, curr_candle.index)
        return True

      return False

    def close_trade(self, sell_price, sell_index):
      self.sell_price = sell_price
      self.sell_index = sell_index
      self.profit = self.sell_price - self.buy_price

      self.is_closed = True
