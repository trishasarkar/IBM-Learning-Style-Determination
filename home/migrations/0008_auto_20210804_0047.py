# Generated by Django 3.1.4 on 2021-08-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userdata_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='msg_feed',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='uage',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='uname',
            field=models.CharField(default='', max_length=150),
        ),
    ]