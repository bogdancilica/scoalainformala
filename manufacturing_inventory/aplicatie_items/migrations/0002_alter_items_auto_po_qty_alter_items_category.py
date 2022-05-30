# Generated by Django 4.0.4 on 2022-05-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='auto_po_qty',
            field=models.CharField(choices=[('n_a', 'n/a'), ('5', '5'), ('10', '10'), ('15', '15'), ('20', '20')], max_length=100),
        ),
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('fittings', 'Fittings'), ('adaptors', 'Adaptors'), ('b_valves', 'Ball Valves'), ('c_valves', 'Check Valves'), ('r_valves', 'Relief Valves'), ('p_indicators', 'Pressure Indicators'), ('t_indicators', 'Temperature Indicators')], max_length=100),
        ),
    ]