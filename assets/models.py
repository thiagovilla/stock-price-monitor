from django.db import models


class Asset(models.Model):
    """An asset with a symbol and current price"""
    symbol = models.CharField(max_length=200)
    current_price = models.FloatField(default=0)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Asset object"""
        return self.symbol


class TrackedAsset(models.Model):
    """A tracked assset with lower and upper limit prices"""
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    lower_limit = models.FloatField(default=0)
    upper_limit = models.FloatField(default=0)

    def __str__(self):
        """String for representing the TrackedAsset object"""
        return f'{self.asset.symbol} ({self.lower_limit:.2f}-{self.upper_limit:.2f})'
