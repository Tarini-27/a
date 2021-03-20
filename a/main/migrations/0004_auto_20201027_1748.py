# Generated by Django 3.0.1 on 2020-10-27 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='active',
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('final_total', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
                ('sec1_total', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
                ('sec2_total', models.DecimalField(decimal_places=0, default=0, max_digits=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
