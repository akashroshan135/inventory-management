from django.contrib import admin
from .models import Stock, Purchase

#class ForumAdmin(admin.ModelAdmin):
#    list_display = ('name', 'forum_type', 'forum')
#    list_filter = ('forum_type', 'issubforum')

admin.site.register(Stock)                                  # shows the Stock that are created in the admin page
admin.site.register(Purchase)                               # shows the Purchase that are created in the admin page