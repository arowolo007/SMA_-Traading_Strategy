from binance.client import Client

api_key = 'sJy00CQL0OeK0yn6G07rP96MIhNCa5CdBj4S6dps4ndZogBYGOl4D05n9xVpqp7U'
api_secret = 'R54EeaARf9Q3CmFnDleR2589JVEXqdBdlLS8bDWgzDlCgl39c2jPNBKyKXfAkbeX'

client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# # place a test market buy order, to place an actual order use the create_order function
# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=Client.SIDE_BUY,
#     type=Client.ORDER_TYPE_MARKET,
#     quantity=100)
