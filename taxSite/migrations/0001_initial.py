# Generated by Django 2.0.5 on 2018-05-06 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_prove_num', models.CharField(max_length=32)),
                ('taxpayer_name', models.CharField(max_length=32)),
                ('issuing_date', models.DateField()),
                ('taxpayer_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_tag', models.CharField(max_length=32)),
                ('declaration_date', models.DateField()),
                ('declaration_income', models.FloatField()),
                ('paid_up_tax_amount', models.FloatField()),
                ('tax_start_time', models.DateField()),
                ('tax_end_time', models.DateField()),
                ('tax_prove_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxSite.List')),
            ],
        ),
    ]
