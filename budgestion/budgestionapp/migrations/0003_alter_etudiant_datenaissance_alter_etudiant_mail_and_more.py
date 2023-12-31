# Generated by Django 4.2.2 on 2023-07-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgestionapp", "0002_alter_etudiant_budget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etudiant",
            name="dateNaissance",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="etudiant",
            name="mail",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="etudiant",
            name="nom",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="etudiant",
            name="prenom",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
