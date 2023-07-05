# Generated by Django 4.2.3 on 2023-07-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_movie_actors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(related_name="movies", to="movies.actor"),
        ),
    ]
