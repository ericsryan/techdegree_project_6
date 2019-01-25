from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    caption = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=300)
    order = models.IntegerField(default=0)
    mineral = models.ForeignKey(Mineral,
                                models.SET_NULL,
                                blank=True,
                                null=True)

    def __str__(self):
        return self.name + ": " + self.content
