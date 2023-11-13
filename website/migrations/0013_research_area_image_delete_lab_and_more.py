# Generated by Django 4.2.2 on 2023-09-06 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_remove_research_scholar_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='research_area_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='research_area')),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Reseach Area Image',
                'verbose_name_plural': 'Reseach Area Images',
            },
        ),
        migrations.DeleteModel(
            name='lab',
        ),
        migrations.RemoveField(
            model_name='research_area',
            name='description',
        ),
        migrations.AddField(
            model_name='research_area',
            name='broad_research_area',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='research_area',
            name='faculties',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='research_area_image',
            name='research_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.research_area'),
        ),
    ]