from dataclasses import dataclass

@dataclass
class Stats:
    num_trades: int
    win_rate: float
    num_wins: int
    num_losses: int
    perc_return: float
    perc_return_buy_and_hold: float
    initial_cash: float
    total_profit: float
    max_drawdown: float
    max_drawdown_abs: float

    def __repr__(self) ->str:
      return(
          f"Stats("
          f"trades={self.num_trades},"
          f"win_rate={self.win_rate:.2%},"
          f"return={self.perc_return:.2%},"
          f"maxDD={self.max_drawdown:.2%},"
          f"buy&hold={self.perc_return_buy_and_hold:.2%}"
          f")"
      )