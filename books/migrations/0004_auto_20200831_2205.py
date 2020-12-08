# Generated by Django 3.1 on 2020-08-31 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200831_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='average_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='ratings_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.CharField(max_length=25600, null=True),
        ),
    ]