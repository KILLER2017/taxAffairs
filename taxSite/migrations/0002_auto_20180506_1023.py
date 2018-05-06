# Generated by Django 2.0.5 on 2018-05-06 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_prove_num', models.CharField(max_length=32)),
                ('taxpayer_name', models.CharField(max_length=32)),
                ('issuing_date', models.DateField()),
                ('taxpayer_id', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='list',
            old_name='tax_prove_num',
            new_name='check_code',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='issuing_date',
            new_name='print_date',
        ),
        migrations.RemoveField(
            model_name='list',
            name='taxpayer_id',
        ),
        migrations.AddField(
            model_name='list',
            name='taxpayer_idCard_num',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]