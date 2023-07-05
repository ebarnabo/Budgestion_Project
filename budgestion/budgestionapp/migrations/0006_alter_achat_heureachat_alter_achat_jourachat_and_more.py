# Generated by Django 4.2.2 on 2023-07-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("budgestionapp", "0005_achat_descriptionachat_revenu_descriptionrevenu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="achat",
            name="heureAchat",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="achat",
            name="jourAchat",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="revenu",
            name="heureRevenu",
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="revenu",
            name="jourRevenu",
            field=models.DateField(blank=True, null=True),
        ),
    ]
