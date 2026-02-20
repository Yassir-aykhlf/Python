import random
import time
import inspect
import itertools
from datetime import datetime
from typing import Generator, Iterator, TypedDict

class MarketTick(TypedDict):
    symbol: str
    price: int
    timestamp: str

# Finite State Machine Coroutine
def trading_bot() -> Generator[None, int, None]:
    state: str = "WATCHING"
    print(f"Bot initialized in state: {state}")
    try:
        while True:
            try:
                price: int = (yield)
            except ValueError as e:
                print(f"Alert: {e}. Resetting...")
                state = "WATCHING"
                continue
            
            if state == "WATCHING":
                if price < 100:
                    print(f"Price ${price}: Dip detected, buying...")
                    state = "ACTIVE"
                else:
                    print(f"price ${price}, waiting for a dip...")
            elif state == "ACTIVE":
                if price > 150:
                    print(f"Price ${price}: Spike detected, selling...")
                    state = "WATCHING"
                else:
                    print(f"Price ${price}, waiting for a spike...")
    except GeneratorExit:
        print("Bot Exiting...")

def market_ticker() -> Iterator[MarketTick]:
    stocks: list[str] = ['AAPL', 'GOOG', 'TSLA', 'AMZN']
    while True:
        symbol: str = random.choice(stocks)
        price: int = random.randint(-10, 200)
        yield {
            'symbol': symbol,
            'price': price,
            'timestamp': datetime.now().isoformat()
        }
        time.sleep(0.1)

def invalid_price(price: int) -> bool:
    return price < 0

if __name__ == "__main__":
    ticker: Iterator[MarketTick] = market_ticker()
    aapl_stream: Iterator[MarketTick] = (
        data for data in ticker if data['symbol'] == 'AAPL'
    )
    
    bot: Generator[None, int, None] = trading_bot()

    print(f"Bot State: {inspect.getgeneratorstate(bot)}")
    next(bot)
    print(f"Bot State: {inspect.getgeneratorstate(bot)}")
    print("-" * 42)

    print(f"Starting High Frequency Pipeline...\n")
    for tick in itertools.islice(aapl_stream, 10):
        current_price: int = tick['price']
        if invalid_price(current_price):
            bot.throw(ValueError("Corrupted Data Stream"))
        else:
            bot.send(current_price)
    
    bot.close()