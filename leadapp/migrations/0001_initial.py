# Generated by Django 3.1.8 on 2022-06-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('New', 'New'), ('Qualified', 'Qualified'), ('Discussion', 'Discussion'), ('Negotiation', 'Negotiation'), ('Won', 'Won'), ('Lost', 'Lost')], max_length=20)),
                ('owner', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
