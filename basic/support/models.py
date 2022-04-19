from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User =  get_user_model()

class Faq(models.Model):
    CATEGORY_CHOICE = [
        ('일반','일반'),
        ('계정','계정'),
        ('기타','기타'),
    ]
    category = models.CharField(verbose_name='카태고리',max_length=2, choices=CATEGORY_CHOICE, default='일반',)
    question = models.TextField(verbose_name='질문')
    answer = models.TextField(verbose_name='답변')
    create_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    writer = models.ForeignKey(verbose_name='생성자', to=User ,on_delete=models.CASCADE, null=True , blank=True)
    writer_final = models.ForeignKey(verbose_name='최종 수정자', to=User ,on_delete=models.CASCADE, null=True , blank=True, related_name="faq_writer_final")
    final_time = models.DateTimeField(verbose_name='최종 수정일시', auto_now_add=True, blank=True)



