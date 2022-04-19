# Generated by Django 4.0.4 on 2022-04-16 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_ct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ct',
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.CharField(choices=[('일반', '일반'), ('계정', '계정'), ('기타', '기타')], default='일반', max_length=2, verbose_name='카태고리'),
        ),
        migrations.AddField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='faq',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일시'),
        ),
    ]