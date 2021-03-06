# Generated by Django 3.2.9 on 2021-11-18 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_auto_20211118_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='reference_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='sketches',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='play',
            name='reference_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trackers', to='play.play'),
        ),
    ]
