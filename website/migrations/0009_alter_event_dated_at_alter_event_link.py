# Generated by Django 4.2.2 on 2023-07-17 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_event_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dated_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
