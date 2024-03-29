# Generated by Django 3.2.15 on 2022-09-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_packagepurchasehistory_payment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerpetualGrowthRateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('symbol_name', models.CharField(max_length=255)),
                ('symbol_currency', models.CharField(max_length=255)),
                ('revenue_ttm', models.CharField(max_length=255)),
                ('nop_ttm', models.CharField(max_length=255)),
                ('roe', models.CharField(max_length=255)),
                ('roc', models.CharField(max_length=255)),
                ('ke', models.CharField(max_length=255)),
                ('kd', models.CharField(max_length=255)),
                ('ev', models.CharField(max_length=255)),
                ('wacc', models.CharField(max_length=255)),
                ('market_cap', models.CharField(max_length=255)),
                ('perpetual_growth_rate', models.CharField(max_length=255)),
                ('de_ratio', models.CharField(max_length=255)),
                ('beta', models.CharField(max_length=255)),
            ],
        ),
    ]
