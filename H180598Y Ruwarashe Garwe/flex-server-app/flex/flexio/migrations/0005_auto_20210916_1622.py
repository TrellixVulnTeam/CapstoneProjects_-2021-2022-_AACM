# Generated by Django 3.1.11 on 2021-09-16 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flexio', '0004_auto_20210916_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='follow_up_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='follow_up_question', to='flexio.followupquestion'),
        ),
        migrations.AlterField(
            model_name='field',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link', to='flexio.link'),
        ),
        migrations.AlterField(
            model_name='field',
            name='range',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='range', to='flexio.range'),
        ),
    ]
