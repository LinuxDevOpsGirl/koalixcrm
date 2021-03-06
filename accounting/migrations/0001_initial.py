# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.IntegerField(verbose_name='Account Number')),
                ('title', models.CharField(max_length=50, verbose_name='Account Title')),
                ('accountType', models.CharField(choices=[('E', 'Earnings'), ('S', 'Spendings'), ('L', 'Liabilities'), ('A', 'Assets')], max_length=1, verbose_name='Account Type')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('originalAmount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='Original Amount')),
                ('isopenreliabilitiesaccount', models.BooleanField(verbose_name='Is The Open Liabilities Account')),
                ('isopeninterestaccount', models.BooleanField(verbose_name='Is The Open Interests Account')),
                ('isProductInventoryActiva', models.BooleanField(verbose_name='Is a Product Inventory Account')),
                ('isACustomerPaymentAccount', models.BooleanField(verbose_name='Is a Customer Payment Account')),
            ],
            options={
                'ordering': ['accountNumber'],
                'verbose_name': 'Account',
                'verbose_name_plural': 'Account',
            },
        ),
        migrations.CreateModel(
            name='AccountingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('begin', models.DateField(verbose_name='Begin')),
                ('end', models.DateField(verbose_name='End')),
            ],
            options={
                'verbose_name': 'Accounting Period',
                'verbose_name_plural': 'Accounting Periods',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Amount')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Description')),
                ('bookingDate', models.DateTimeField(verbose_name='Booking at')),
                ('dateofcreation', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('lastmodification', models.DateTimeField(auto_now_add=True, verbose_name='Last modified')),
                ('accountingPeriod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.AccountingPeriod', verbose_name='AccountingPeriod')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='ProductCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Product Categorie Title')),
                ('lossAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='db_loss_account', to='accounting.Account', verbose_name='Loss Account')),
                ('profitAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='db_profit_account', to='accounting.Account', verbose_name='Profit Account')),
            ],
            options={
                'verbose_name': 'Product Categorie',
                'verbose_name_plural': 'Product Categories',
            },
        ),
    ]
