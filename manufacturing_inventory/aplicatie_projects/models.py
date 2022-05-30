from django.contrib.auth.models import User
from django.db import models

from aplicatie_items.models import Items


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    reference_number = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    responsible_engineer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.project_name}"
