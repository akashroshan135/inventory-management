from django.contrib import admin
from .models import Stock

#class ForumAdmin(admin.ModelAdmin):
#    list_display = ('name', 'forum_type', 'forum')
#    list_filter = ('forum_type', 'issubforum')

admin.site.register(Stock)