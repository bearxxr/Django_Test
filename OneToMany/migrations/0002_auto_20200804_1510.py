# Generated by Django 2.2.14 on 2020-08-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OneToMany', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OneToMany.Dept'),
        ),
    ]
