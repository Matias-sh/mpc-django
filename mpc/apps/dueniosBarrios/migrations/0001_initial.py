# Generated by Django 4.1 on 2022-08-25 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0002_personas_delete_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='DueniosBarrios',
            fields=[
                ('id_dueniobarrio', models.AutoField(primary_key=True, serialize=False)),
                ('detalle_duenio', models.TextField()),
                ('id_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.personas')),
            ],
        ),
    ]
