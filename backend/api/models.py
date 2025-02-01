from django.db import models

class Client(models.Model):
    PRIORITY_CHOICES = [('speed', 'Speed'), ('accuracy', 'Accuracy')]

    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    punctuality_rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.name

class Translator(models.Model):
    name = models.CharField(max_length=100)
    languages = models.JSONField()
    accuracy_rating = models.FloatField(default=5.0)
    speed_rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.name
