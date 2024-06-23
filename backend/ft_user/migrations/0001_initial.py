# Generated by Django 5.0.6 on 2024-06-23 01:57

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import django_prometheus.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True)),
                ('otp_enabled', models.BooleanField(default=False, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=1024, null=True)),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('multi_nickname', models.CharField(blank=True, max_length=128, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=(django_prometheus.models.ExportModelOperationsMixin('user'), models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FollowList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_username', models.CharField(blank=True, max_length=128, null=True)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('follow_list'), models.Model),
        ),
        migrations.CreateModel(
            name='SingleGameRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('player1_score', models.IntegerField()),
                ('player2_score', models.IntegerField()),
                ('is_tournament', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('winner', models.CharField(blank=True, max_length=128, null=True)),
                ('player1', models.ForeignKey(blank=True, db_column='player1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(blank=True, db_column='player2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('game_record'), models.Model),
        ),
        migrations.CreateModel(
            name='SingleGameDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('goal_user_name', models.CharField(max_length=128)),
                ('goal_user_position', models.CharField(max_length=128)),
                ('ball_start_position', models.CharField(max_length=255)),
                ('ball_end_position', models.CharField(max_length=255)),
                ('timestamp', models.FloatField()),
                ('game', models.ForeignKey(db_column='game', on_delete=django.db.models.deletion.CASCADE, to='ft_user.singlegamerecord')),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('game_detail'), models.Model),
        ),
        migrations.CreateModel(
            name='MultiGameRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('player1', models.ForeignKey(blank=True, db_column='player1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1_multi', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(blank=True, db_column='player2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2_multi', to=settings.AUTH_USER_MODEL)),
                ('player3', models.ForeignKey(blank=True, db_column='player3', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3_multi', to=settings.AUTH_USER_MODEL)),
                ('player4', models.ForeignKey(blank=True, db_column='player4', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4_multi', to=settings.AUTH_USER_MODEL)),
                ('game1', models.ForeignKey(blank=True, db_column='game1', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game1', to='ft_user.singlegamerecord')),
                ('game2', models.ForeignKey(blank=True, db_column='game2', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game2', to='ft_user.singlegamerecord')),
                ('game3', models.ForeignKey(blank=True, db_column='game3', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game3', to='ft_user.singlegamerecord')),
            ],
        ),
    ]
