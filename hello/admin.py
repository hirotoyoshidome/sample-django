from django.contrib import admin
from .models import Question, Choice

# リレーションが貼られているため、管理画面でもインラインでデータを挿入できるように変更する(admin.StackedInlineではなくこちらを継承する)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # DBインサート時の管理画面からのフィールドの並び順を変更する
    # fields = ['pub_date', 'question_text']
    # こちらは分割して並び替えをする
    fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date Information', {'fields': ['pub_date'],
                                  'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
