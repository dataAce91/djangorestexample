# Generated by Django 3.1.3 on 2020-11-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='text_reviews_count',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
