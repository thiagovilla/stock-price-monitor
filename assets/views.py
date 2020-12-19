from django.http import HttpResponse
from django.conf import settings
import requests


def index(request):
    return HttpResponse("This is the assets index")


def details(request, asset_symbol):
    response = requests.get(
        f'https://api.hgbrasil.com/finance/stock_price?key={settings.HG_API_KEY}&symbol={asset_symbol}')

    if (not response.ok):
        return HttpResponse(f'Request error: {response.text()}')

    results = response.json().get('results')

    if ('error' in results):
        return HttpResponse(f'Invalid symbol error: {results.get("message")}')

    symbol_data = results.get(asset_symbol)

    if ('error' in symbol_data):
        return HttpResponse(f'Symbol not found: {symbol_data.get("message")}')

    price = symbol_data.get('price')
    return HttpResponse(f'Current price for {asset_symbol}: {price:.2f}')
