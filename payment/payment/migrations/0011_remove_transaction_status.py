# Generated by Django 4.0.6 on 2022-07-25 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_alter_product_options_remove_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='status',
        ),
    ]
