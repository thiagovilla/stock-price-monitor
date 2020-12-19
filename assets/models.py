from django.db import models

class Asset(models.Model):
    """A tracked asset with lower and upper price limits"""
    symbol = models.CharField(max_length=200)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    current_price = models.FloatField(default=0)

    def __str__(self):
        """String for representing the Asset object (e.g. in Admin site)."""
        return self.symbol