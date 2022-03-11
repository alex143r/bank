# Generated by Django 4.0.3 on 2022-03-11 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_rank_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.ForeignKey(choices=[(0, 'Basic'), (1, 'Silver'), (2, 'Gold')], default=0, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='bank.rank'),
        ),
    ]