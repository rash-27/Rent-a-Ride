# Generated by Django 4.2.6 on 2023-11-05 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_transactions_uniq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='uniq',
            field=models.CharField(max_length=10),
        ),
    ]