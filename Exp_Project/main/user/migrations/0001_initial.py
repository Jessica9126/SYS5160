# Generated by Django 4.1.2 on 2022-11-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=32)),
                ('phone_number', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('doctor', models.CharField(max_length=32, null=True)),
                ('comment', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('introduction', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('clinic_number', models.CharField(max_length=255)),
                ('clinic_picture', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdate', models.DateField(null=True)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('status', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('password', models.CharField(max_length=64, verbose_name='password')),
                ('age', models.IntegerField(null='true', verbose_name='age')),
                ('email', models.CharField(max_length=64, verbose_name='email')),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'unknown')], null='true', verbose_name='gender')),
                ('appointment', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='user.doctor', verbose_name='appointment')),
            ],
        ),
    ]
