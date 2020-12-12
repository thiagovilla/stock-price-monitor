from django.db import models

class Assets(models.Model):
    """A tracked asset with lower and upper price limits"""
    name = models.CharField(max_length=200)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()

    def __str__(self):
        """String for representing the Asset object (e.g. in Admin site)."""
        return self.name