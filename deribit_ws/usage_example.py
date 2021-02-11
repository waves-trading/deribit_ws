import asyncio
from .deribit_ws import deribit

der_inst = deribit(
    config={
        "apiKey": "KEY",
        "secret": "SECRET",
        "ws_url": 'wss://www.deribit.com/ws/api/v2'
    }
)


async def main():
    async with der_inst as ws_conn:
        async with ws_conn as conncetion:
            der_inst.ws_descriptor = conncetion
            await der_inst.login_ws()
            # print(conncetion)
            # print(conncetion.open)
            # print(der_inst.ws_descriptor)
            # print(der_inst.ws_descriptor.open)
            # await der_inst.fetch_time()
            # await der_inst.fetch_status()
            # await der_inst.load_markets()
            # print(der_inst.markets)
            # b = await der_inst.fetch_balance()
            # print(b)
            # b = await der_inst.fetch_balance()
            # b = await der_inst.create_deposit_address("BTC")
            # b = await der_inst.fetch_tickers()
            # await der_inst.load_markets()
            # print(der_inst.markets)
            # b = await der_inst.fetch_ticker("BTC-24SEP21-56000-P")
            # b = await der_inst.fetch_ohlcv("BTC-24SEP21-56000-P", limit=10)
            # b = await der_inst.fetch_trades("BTC-5FEB21-55000-P")
            # b = await der_inst.fetch_order_book("BTC-5FEB21-55000-P")
            # b = await der_inst.fetch_order_book("BTC-5FEB21-55000-P")
            # print(b)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
