# Generated by Django 3.1.5 on 2021-10-12 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('logid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.signin')),
            ],
        ),
    ]