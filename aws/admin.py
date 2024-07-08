from django.contrib import admin
from .models import aws

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_answer')
    list_filter = ('correct_answer',)
    search_fields = ('question_text',)

admin.site.register(aws, QuestionAdmin)
