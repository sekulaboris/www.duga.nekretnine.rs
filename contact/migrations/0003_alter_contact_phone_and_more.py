# Generated by Django 4.2.5 on 2023-09-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_question_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='question_categories',
            field=models.CharField(choices=[('nekretnine', 'Nekretnine'), ('prodaja', 'Prodaja'), ('kupovina', 'Kupovina'), ('kuće', 'Kuće'), ('stanovi', 'Stanovi'), ('ugovori i dokumentacija', 'Ugovori i dokumentacija'), ('ostalo', 'Ostalo')], default='nekretnine', max_length=50, verbose_name='How can we help you?'),
        ),
    ]
