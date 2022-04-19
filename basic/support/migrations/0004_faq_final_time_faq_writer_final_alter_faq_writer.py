# Generated by Django 4.0.4 on 2022-04-19 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_delete_ct_faq_category_faq_writer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='final_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='최종 수정일시'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='writer_final',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_writer_final', to=settings.AUTH_USER_MODEL, verbose_name='최종 수정자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='생성자'),
        ),
    ]
