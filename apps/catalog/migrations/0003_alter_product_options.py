# Generated by Django 5.0.6 on 2024-08-13 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_change_published', 'Can change is_published status'), ('can_change_description', 'Can change description'), ('can_change_category', 'Can change category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]