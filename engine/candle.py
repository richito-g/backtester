from dataclasses import dataclass

@dataclass
class Candle:
    open: float
    high: float
    close: float
    low: float
    index: int