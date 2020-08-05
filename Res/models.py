from django.db import models


# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'res_animal'

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }
