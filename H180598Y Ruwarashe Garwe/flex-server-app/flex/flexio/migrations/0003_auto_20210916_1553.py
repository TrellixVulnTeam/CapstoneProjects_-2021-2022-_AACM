# Generated by Django 3.1.11 on 2021-09-16 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flexio', '0002_auto_20210916_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section', to='flexio.assessmenttemplate'),
        ),
    ]
