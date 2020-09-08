# Generated by Django 3.1 on 2020-09-01 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0004_auto_20200901_0830'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.music')),
            ],
        ),
    ]