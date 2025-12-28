from data.load_data import load_price_data
from strategies.random_strategy import RandomStrategy
from engine.backtest import run_backtest
from analysis.stats import compute_stats
from analysis.plot import plot_equity_curve

def main():
    candles = load_price_data()
    strategy = RandomStrategy(prob=0.05)
    portfolio = run_backtest(
        candles,
        strategy,
        initial_cash = 1000000,
        profit_perc = .02,
        stop_loss_perc = .01,
        fraction_of_cash = .25
    )
    
    stats = compute_stats(portfolio, candles)
    print(stats)
    print("Final equity:", portfolio.equity_curve[-1])
    print("Number of closed trades:",len(portfolio.closed_trades))

    plot_equity_curve(portfolio)



if __name__== "__main__":
    main()