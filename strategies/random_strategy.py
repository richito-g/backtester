import numpy as np
from engine.strategy import BaseStrategy
from engine.candle import Candle

class RandomStrategy(BaseStrategy):
  def __init__(self, prob:float = .05, seed:int = 42):
    self.prob = prob
    self.rng = np.random.default_rng(seed)

  def should_enter(self, candle: Candle) -> bool:
    return self.rng.random() <self.prob