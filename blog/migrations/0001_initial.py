# Generated by Django 4.2.6 on 2023-10-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('resumo', models.CharField(max_length=250)),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
    ]
