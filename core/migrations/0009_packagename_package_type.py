# Generated by Django 4.1 on 2022-08-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_packagepurchasehistory_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagename',
            name='package_type',
            field=models.CharField(blank=True, choices=[('free', 'Free Membership'), ('pro_paid', 'Pro Membership')], max_length=255, null=True),
        ),
    ]
