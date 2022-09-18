import requests


# In this example, notice there is no @ character involved. With the __call__ method the decorator is executed when
# an instance of the class is created.

# This class keeps track of the number of times a function to query to an API has been run. Once it reaches the limit
# the decorator stops the function from executing.


class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return


@LimitQuery
def get_coin_price(limit):
    """View the Bitcoin Price Index (BPI)"""

    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


if __name__ == '__main__':
    print(get_coin_price(5))
    print(get_coin_price(5))
    print(get_coin_price(5))
    print(get_coin_price(5))
    print(get_coin_price(5))
    print(get_coin_price(5))
