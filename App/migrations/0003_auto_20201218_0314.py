# Generated by Django 3.1.4 on 2020-12-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20201218_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[(1, 'Easy'), (2, 'Medi'), (3, 'Hard')], default=1, max_length=4),
        ),
    ]
