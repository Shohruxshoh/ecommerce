# Generated by Django 3.1.6 on 2021-02-02 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210202_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
