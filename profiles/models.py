from django.db import models
from author.models import Author
# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=30)
    about=models.TextField()
    author=models.OneToOneField(Author,on_delete=models.CASCADE,default=None)

    def __str__(self) -> str:
        return f"Name---{self.name}"
