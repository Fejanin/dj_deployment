from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=100)
    describe = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name