# Generated by Django 2.1.7 on 2019-07-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('orderName', models.CharField(max_length=50)),
                ('orderPayee', models.CharField(max_length=50)),
                ('orderPhone', models.IntegerField()),
                ('orderAllPrice', models.CharField(max_length=50)),
                ('orderPrice', models.CharField(max_length=50)),
                ('orderStatus', models.CharField(max_length=50)),
                ('orderPayStatus', models.CharField(max_length=50)),
                ('orderPayType', models.CharField(max_length=50)),
                ('orderDeliveryStatus', models.CharField(max_length=50)),
                ('orderDistributionlogistics', models.CharField(max_length=50)),
            ],
        ),
    ]
