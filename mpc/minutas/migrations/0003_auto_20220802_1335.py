# Generated by Django 3.2.6 on 2022-08-02 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minutas', '0002_cuota_remove_barriodet_id_barrio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id_barrio', models.AutoField(primary_key=True, serialize=False)),
                ('mz', models.IntegerField()),
                ('pc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BarrioDet',
            fields=[
                ('id_barrio_det', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_barrio', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('detalle_cliente', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteBarrio',
            fields=[
                ('id_cliente_barrio', models.AutoField(primary_key=True, serialize=False)),
                ('cant_cuotas', models.IntegerField()),
                ('id_barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.barrio')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteBarrioCuotas',
            fields=[
                ('id_cliente_barrio_det', models.AutoField(primary_key=True, serialize=False)),
                ('nro_cuota', models.IntegerField()),
                ('tipo_cuota', models.CharField(choices=[('Cuota', 'Cuota'), ('Cta. derecho posesion', 'Cta. derecho posesion'), ('Adelanto cuota', 'Adelanto cuota')], max_length=40)),
                ('cuota_total_pesos', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('cuota_mas_interes', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('porcentaje_gastos', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('gastos_pesos', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('porcentaje_interes', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('interes_pesos', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('detalle', models.CharField(max_length=500)),
                ('observaciones', models.CharField(max_length=500)),
                ('tipo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Credito', 'Credito'), ('Cheque', 'Cheque'), ('Transferencia', 'Transferencia')], max_length=40)),
                ('detalle_cliente_barrio_det', models.CharField(max_length=200)),
                ('id_cliente_barrio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.clientebarrio')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleMinuta',
            fields=[
                ('id_detalle_minuta', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DueñoBarrio',
            fields=[
                ('id_dueño_barrio', models.AutoField(primary_key=True, serialize=False)),
                ('detalle_dueño_barrio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('id_efectivo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.DecimalField(decimal_places=2, max_digits=9999)),
            ],
        ),
        migrations.CreateModel(
            name='MinutaGeneral',
            fields=[
                ('id_minuta_general', models.AutoField(primary_key=True, serialize=False)),
                ('importe_minuta', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('diferencia', models.DecimalField(decimal_places=2, max_digits=9999)),
                ('id_detalle_minuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.detalleminuta')),
                ('id_efectivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.efectivo')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('fecha_nac', models.DateField()),
                ('detalle_persona', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tipo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=20)),
                ('constrasenia', models.CharField(max_length=30)),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.persona')),
            ],
        ),
        migrations.DeleteModel(
            name='Cuota',
        ),
        migrations.AddField(
            model_name='minutageneral',
            name='id_tipo_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.tipopago'),
        ),
        migrations.AddField(
            model_name='minutageneral',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.usuario'),
        ),
        migrations.AddField(
            model_name='dueñobarrio',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.persona'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.persona'),
        ),
        migrations.AddField(
            model_name='barriodet',
            name='id_dueño_barrio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.dueñobarrio'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='id_barrio_det',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minutas.barriodet'),
        ),
    ]
