from django.contrib import admin
from .models import Question,Choices,Voter

class choiceInline(admin.StackedInline):
	model = Choices
	extra = 2

class questionAdmin(admin.ModelAdmin):
	list_display = ('question_text','pub_date')
	list_filter = ['pub_date']
	inlines = [choiceInline]


admin.site.register(Question,questionAdmin)
admin.site.register(Choices)
admin.site.register(Voter)

