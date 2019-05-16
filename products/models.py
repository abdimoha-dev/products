from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=100)
    summary=models.TextField(default='This is cool')

    class Meta:
        db_table= 'prod'

    def __str__(self):
        return self.title
