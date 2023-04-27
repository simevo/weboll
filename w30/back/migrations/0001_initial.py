# Generated by Django 4.0.5 on 2022-08-03 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0011_auto_20220715_1655"),
    ]

    operations = [
        migrations.CreateModel(
            name="AreeAllertamento",
            fields=[
                (
                    "id_allertamento",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("id_area", models.IntegerField()),
                ("descrizione", models.CharField(blank=True, max_length=50, null=True)),
                ("codice_istat_reg", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "aree_allertamento",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ForecastZone",
            fields=[
                (
                    "id_forecast_zone",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("model_name", models.CharField(max_length=9)),
                ("model_type", models.CharField(max_length=5)),
                ("data_emissione", models.DateTimeField()),
                ("data_riferimento", models.DateTimeField()),
                (
                    "valore_originale",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=12, null=True
                    ),
                ),
                (
                    "valore_validato",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=12, null=True
                    ),
                ),
                ("last_update", models.DateTimeField()),
                ("username", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "forecast_zone",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="W30",
            fields=[
                ("id_w30", models.AutoField(primary_key=True, serialize=False)),
                ("seq_num", models.BigIntegerField(blank=True, null=True)),
                ("data_emissione", models.DateTimeField()),
                ("data_prossimo_aggiornamento", models.DateTimeField()),
                ("status", models.CharField(max_length=1)),
                ("last_update", models.DateTimeField()),
                ("username", models.CharField(max_length=30)),
                ("id_w30_parent", models.IntegerField(blank=True, null=True)),
                ("firstguess", models.TextField(blank=False, null=False)),
            ],
            options={
                "db_table": "w30",
            },
        ),
        migrations.CreateModel(
            name="W30Data",
            fields=[
                ("id_w30_data", models.AutoField(primary_key=True, serialize=False)),
                ("numeric_value", models.IntegerField(blank=True, null=True)),
                (
                    "id_aggregazione",
                    models.ForeignKey(
                        db_column="id_aggregazione",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.aggregazione",
                    ),
                ),
                (
                    "id_allertamento",
                    models.ForeignKey(
                        db_column="id_allertamento",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="w30_back.areeallertamento",
                    ),
                ),
                (
                    "id_parametro",
                    models.ForeignKey(
                        db_column="id_parametro",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.parametro",
                    ),
                ),
                (
                    "id_time_layouts",
                    models.ForeignKey(
                        db_column="id_time_layouts",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.timelayouts",
                    ),
                ),
                (
                    "id_w30",
                    models.ForeignKey(
                        db_column="id_w30",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="w30_back.w30",
                    ),
                ),
            ],
            options={
                "db_table": "w30_data",
            },
        ),
    ]
