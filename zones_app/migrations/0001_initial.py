# Generated by Django 5.2 on 2025-04-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zones/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_type', models.CharField(choices=[('day', 'Сутки'), ('hour', 'Часы')], default='day', max_length=10)),
                ('capacity', models.IntegerField(default=1)),
            ],
        ),
    ]
