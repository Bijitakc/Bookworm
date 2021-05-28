from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Book(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    desc=models.TextField()
    # slug=models.SlugField(max_length=250)
    #add genres
    GENRE_CHOICES=(
        ('Fantasy','Fantasy'),
        ('Thriller','Thriller'),
        ('Romance','Romance'),
        ('Mystery','Mystery'),
        ('Horror',"Horror"),
        ('Fiction','Fiction'),
        ('NonFiction','NonFiction'),
        ('Comics','Comics'),
        ('Science Fiction','Science Fiction'),
        ('Young Adult','Young Adult'),
    )
    genre=models.CharField(max_length=20,choices=GENRE_CHOICES)
    CONDITION_CHOICES=(
        ('Good','G'),
        ('Average','A'),
        ('Poor','P'),
    )
    condition=models.CharField(max_length=8,choices=CONDITION_CHOICES)

    class Meta:
        verbose_name="Book"
        verbose_name_plural="Books"

    def __str__(self):
        return self.title
    





