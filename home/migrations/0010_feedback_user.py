# Generated by Django 3.1.4 on 2021-08-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210804_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='home.userdata'),
        ),
    ]
