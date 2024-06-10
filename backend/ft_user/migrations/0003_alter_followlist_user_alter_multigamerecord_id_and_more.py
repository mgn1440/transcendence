# Generated by Django 5.0.6 on 2024-06-10 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft_user', '0002_singlegamedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followlist',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='multigamerecord',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='multigamerecord',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='singlegamedetail',
            name='game',
            field=models.ForeignKey(db_column='GameRecord', on_delete=django.db.models.deletion.CASCADE, to='ft_user.singlegamerecord'),
        ),
        migrations.AlterField(
            model_name='singlegamerecord',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='singlegamerecord',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
