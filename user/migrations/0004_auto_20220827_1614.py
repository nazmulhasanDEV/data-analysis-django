# Generated by Django 3.2 on 2022-08-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_account_membership_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='membershipEndingDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='membershipStartingDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
