# Generated by Django 2.2 on 2019-05-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgboard', '0001_Post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('user_name', models.TextField()),
                ('user_id', models.IntegerField()),
                ('up_or_down', models.CharField(max_length=1)),
            ],
        ),
    ]