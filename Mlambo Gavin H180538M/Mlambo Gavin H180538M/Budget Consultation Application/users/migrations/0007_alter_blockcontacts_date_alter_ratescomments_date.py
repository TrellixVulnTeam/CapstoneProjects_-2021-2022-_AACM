<<<<<<< HEAD
# Generated by Django 4.0.1 on 2022-03-08 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_ratescomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockcontacts',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='ratescomments',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
=======
# Generated by Django 4.0.1 on 2022-03-08 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_ratescomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockcontacts',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='ratescomments',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
>>>>>>> parent of 5a30ca7... commit message