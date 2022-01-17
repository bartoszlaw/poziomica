from django.db import models

class Pomiary(models.Model):
    nazwa = models.CharField(max_length=100)
    wynik = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazwa

