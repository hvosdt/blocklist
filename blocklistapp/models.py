from django.db import models

class Item (models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("pub_date")
    rank = models.IntegerField(default=0)
