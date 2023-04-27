# Generated by Django 4.1.7 on 2023-04-27 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0002_alter_goalcategory_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего обновления')),
                ('text', models.TextField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goals.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]