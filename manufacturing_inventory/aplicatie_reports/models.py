from django.contrib.auth.models import User
from django.db import models

from aplicatie_items.models import Items
from aplicatie_projects.models import Projects


class Reports(models.Model):
    item_no = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.item_no} - {self.quantity}"