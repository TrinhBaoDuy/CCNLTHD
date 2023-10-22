from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    ngaytao = models.DateField(auto_now_add=True, null=True)
    ngaysua = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)


    def __str__(self):
        return self.name

class Course(BaseModel):
    monhoc = models.CharField(max_length=255, null=False)
    mota = models.TextField()
    hinhanh = models.CharField(max_length=100)

    def __str__(self):
        return self.monhoc