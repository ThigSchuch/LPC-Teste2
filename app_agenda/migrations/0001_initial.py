# Generated by Django 2.1.7 on 2019-03-30 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('visibilidade', models.BooleanField(default=False, verbose_name='Tornar privado?')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaInstitucional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Título')),
                ('data', models.DateField(verbose_name='Dia marcado')),
                ('hora', models.TimeField(verbose_name='Hora')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
        ),
        migrations.AddField(
            model_name='agendainstitucional',
            name='compromisso',
            field=models.ManyToManyField(to='app_agenda.Compromisso'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='compromisso',
            field=models.ManyToManyField(to='app_agenda.Compromisso'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='criador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_agenda.Pessoa'),
        ),
    ]
