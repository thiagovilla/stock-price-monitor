from django.http import HttpResponse
from django.conf import settings

def index(request):
    return HttpResponse("This is the assets index")

def details(request, asset_symbol):
    import requests
    response = requests.get(f'https://api.hgbrasil.com/finance/stock_price?key={settings.HG_API_KEY}&symbol={asset_symbol}')
    price = response.json().get('results').get(asset_symbol).get('price')
    return HttpResponse(f'Current price for {asset_symbol}: {price:.2f}')