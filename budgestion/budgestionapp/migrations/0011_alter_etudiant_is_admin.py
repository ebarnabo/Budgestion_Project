# Generated by Django 4.2.2 on 2023-07-07 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgestionapp", "0010_etudiant_etablissement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etudiant",
            name="is_admin",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
