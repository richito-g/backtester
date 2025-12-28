from engine.strategy import BaseStrategy
from engine.candle import Candle

class EMACrossoverStrategy(BaseStrategy):
    def __init__(self, short_period: int = 20, long_period: int = 50):
        self.short_period = short_period
        self.long_period = long_period

        self.short_ema = None
        self.long_ema = None

        self.prev_short_ema = None
        self.prev_long_ema = None

    def update_ema(self, price: float, prev_ema: float | None, period: int) -> float:
        alpha = 2/(period + 1)
        if prev_ema is None:
            return price
        return alpha * price + (1 - alpha) * prev_ema

    def should_enter(self, candle) -> bool:
        price = candle.close

        prev_short_ema = self.short_ema
        prev_long_ema = self.long_ema

        self.short_ema = self.update_ema(price, self.short_ema, self.short_period)
        self.long_ema = self.update_ema(price, self.long_ema, self.long_period)

        if prev_short_ema is None or prev_long_ema is None:
            return False
        
        crossed_up = prev_short_ema <= prev_long_ema and self.short_ema > self.long_ema

        return crossed_up


        
      