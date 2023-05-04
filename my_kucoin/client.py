from my_kucoin.margin.margin import MarginData
from my_kucoin.market.market import MarketData
from my_kucoin.trade.trade import TradeData
from my_kucoin.user.user import UserData
from my_kucoin.ws_token.token import GetToken


class User(UserData):
    pass


class Trade(TradeData):
    pass


class Market(MarketData):
    pass


class Margin(MarginData):
    pass


class WsToken(GetToken):
    pass


