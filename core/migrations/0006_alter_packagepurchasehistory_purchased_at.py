# Generated by Django 4.1 on 2022-08-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_packagepurchasehistory_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagepurchasehistory',
            name='purchased_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
