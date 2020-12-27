# Generated by Django 3.1.4 on 2020-12-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20201218_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameId',
            field=models.CharField(choices=[('1', 'brickbreaker'), ('2', 'flappy'), ('3', 'pianotiles'), ('4', 'twotho'), ('5', 'typing')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='node',
            name='nodeNumber',
            field=models.CharField(choices=[('1', 'MbandP'), ('2', 'Nan'), ('3', 'FnH'), ('4', 'HCC'), ('5', 'SJA'), ('6', 'LHCC')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], default=1, max_length=1),
        ),
    ]
