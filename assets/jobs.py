import requests
import django
from django.conf import settings

django.setup()

# fmt: off
from assets.models import Asset
# fmt: on


def update_prices():
    for asset in Asset.objects.all():
        response = requests.get(
            'https://api.hgbrasil.com/finance/stock_price?' +
            f'key={settings.HG_API_KEY}&symbol={asset.symbol}')

        if not response.ok:
            # todo handle error
            continue

        results = response.json().get('results')

        if 'error' in results:
            # todo handle error
            continue

        symbol_data = results.get(asset.symbol)

        if 'error' in symbol_data:
            # todo handle error
            continue

        price = symbol_data.get('price')
        asset.current_price = price
        asset.save()
        print(f'Current price for asset {asset.symbol} updated to {price}')
