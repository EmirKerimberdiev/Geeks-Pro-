from django.db import models


class GeeksModel(models.Model):
    id = models.AutoField(primary_key=True)
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
