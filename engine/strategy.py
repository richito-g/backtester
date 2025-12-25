from engine.candle import Candle

class BaseStrategy:
  def should_enter(self, candle: Candle) ->bool:
    raise NotImplementedError