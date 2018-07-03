#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests
from datetime import datetime

btc_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
eth_api_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
white = (255, 255, 255)
gray = (127, 127, 127)
green = (0, 255,   0)
yellow = (255, 255,   0)
red = (255,   0,   0)
blue = (0,   0, 255)


def get_latest_btc_price():
    response = requests.get(btc_api_url)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])


def get_latest_eth_price():
    response = requests.get(eth_api_url)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])


btc_price = get_latest_btc_price
eth_price = get_latest_eth_price
date = datetime.now()
ticker_text = '  Time: ' + date + '  BTC: ' + btc_price + '  ETH: ' + eth_price
ticker_text = ticker_text + ticker_text + ticker_text


class RunText(SampleBase):

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = str(ticker_text)

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(
                offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
