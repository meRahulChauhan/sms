from django.db import models
from django.db import models

# Create your models here.
class usertable(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'usertable'
        ordering=['name']

