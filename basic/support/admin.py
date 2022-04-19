from django.contrib import admin

from .models import Faq


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'create_at', 'writer', 'writer_final', 'final_time')

