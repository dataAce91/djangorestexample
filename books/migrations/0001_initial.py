# Generated by Django 3.1.3 on 2020-11-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=60)),
                ('authors', models.CharField(max_length=60)),
                ('average_rating', models.FloatField()),
                ('isbn', models.CharField(blank=True, max_length=30)),
                ('isbn13', models.CharField(max_length=30)),
                ('language_code', models.CharField(max_length=30)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=60)),
            ],
        ),
    ]
