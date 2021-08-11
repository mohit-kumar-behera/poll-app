from django.contrib import admin
from .models import quickPollUser

class userAdmin(admin.ModelAdmin):
	list_display = ('username','dateJoined')
	list_filter = ['dateJoined']

admin.site.register(quickPollUser,userAdmin)
