# Generated by Django 4.2 on 2024-02-24 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('mediacenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytranslation',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mediacenter.icon'),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='translateObject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mediacenter.icon'),
        ),
    ]
