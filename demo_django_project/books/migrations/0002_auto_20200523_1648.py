# Generated by Django 3.0.6 on 2020-05-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='nb_likes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
