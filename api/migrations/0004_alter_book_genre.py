# Generated by Django 3.2 on 2021-05-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_book_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Fiction', 'Fiction'), ('NonFiction', 'NonFiction'), ('Comics', 'Comics'), ('Science Fiction', 'Science Fiction'), ('Young Adult', 'Young Adult')], max_length=20),
        ),
    ]
