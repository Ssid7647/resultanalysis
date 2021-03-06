# Generated by Django 2.1.1 on 2018-09-12 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resultinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_1', models.IntegerField()),
                ('sub_2', models.IntegerField()),
                ('sub_3', models.IntegerField()),
                ('sub_4', models.IntegerField()),
                ('sub_5', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Branch', models.CharField(max_length=500)),
                ('Rollno', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='resultinfo',
            name='studentkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.student_info'),
        ),
    ]
