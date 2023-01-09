# Generated by Django 4.0.5 on 2022-06-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compe', models.CharField(choices=[('PUNT_GLOBAL', 'Puntaje global'), ('MOD_RAZONA_CUANTITAT_PUNT', 'Modulo razonamiento cuantitativo'), ('MOD_LECTURA_CRITICA_PUNT', 'Modulo lectura crítica'), ('MOD_COMPETEN_CIUDADA_PUNT', 'Modulo competencia ciudadana'), ('MOD_INGLES_PUNT', 'Modulo ingles'), ('MOD_COMUNI_ESCRITA_PUNT', 'Modulo comunicación escrita')], default='PUNT_GLOBAL', max_length=255)),
            ],
        ),
    ]