# Generated by Django 4.2.3 on 2023-07-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(to="movies.actor"),
        ),
    ]
