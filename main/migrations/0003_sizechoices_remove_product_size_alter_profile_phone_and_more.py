# Generated by Django 4.2.2 on 2023-07-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profile_address_alter_profile_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='Укажите номер телефона', max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='main.sizechoices', verbose_name='Размер'),
        ),
    ]