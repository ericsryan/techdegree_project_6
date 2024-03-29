# Generated by Django 2.1.5 on 2019-01-27 07:21
import json

from django.db import migrations

from ..models import Mineral, Attribute


def save_minerals_to_db(apps, schema_editor):
    """Add minerals from the .JSON file to the database."""
    with open('minerals.json', encoding='utf-8') as mineral_file:
        data = json.load(mineral_file)

    for mineral in data:
        for key, value in mineral.items():
            if key == 'name':
                mineral = Mineral.objects.create(name=value)
            elif key == 'image caption':
                mineral.caption = value
                mineral.save()
            elif key == 'image filename':
                continue
            else:
                Attribute.objects.create(
                    name=key,
                    content=value,
                    mineral=mineral
                )


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(save_minerals_to_db)
    ]
