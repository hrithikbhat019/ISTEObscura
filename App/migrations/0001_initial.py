# Generated by Django 3.1.4 on 2020-12-31 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField()),
                ('op1', models.TextField(default='')),
                ('op2', models.TextField(default='')),
                ('op3', models.TextField(default='')),
                ('op4', models.TextField(default='')),
                ('ans', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default=1, max_length=1)),
                ('difficulty', models.CharField(choices=[('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], default=1, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('rollNo', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nodeNumber', models.CharField(choices=[('1', 'MbandP'), ('2', 'Nan'), ('3', 'FnH'), ('4', 'HCC'), ('5', 'SJA'), ('6', 'LHCC'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], default=1, max_length=2)),
                ('score', models.IntegerField(default=0)),
                ('visited', models.BooleanField(default=False)),
                ('questIndex', models.IntegerField(default=-1)),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='App.user')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('gameId', models.CharField(choices=[('1', 'brickbreaker'), ('2', 'flappy'), ('3', 'pianotiles'), ('4', 'snake'), ('5', 'typing')], default=1, max_length=1)),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='App.user')),
            ],
        ),
    ]
