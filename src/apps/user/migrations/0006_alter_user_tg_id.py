# Generated by Django 4.0.5 on 2022-10-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_year_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_id',
            field=models.PositiveIntegerField(help_text='Please enter td id...', unique=True),
        ),
    ]
