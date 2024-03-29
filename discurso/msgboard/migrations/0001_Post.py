# Generated by Django 2.2 on 2019-05-07 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('votes_up', models.IntegerField()),
                ('votes_down', models.IntegerField()),
                ('edit_count', models.IntegerField()),
                ('archived', models.BooleanField()),
                ('censored', models.BooleanField()),
                ('root_post_id', models.IntegerField()),
                ('parent_id', models.IntegerField()),
                ('indent', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
