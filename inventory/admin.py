from django.contrib import admin
from .models import Stock, Purchases

#class ForumAdmin(admin.ModelAdmin):
#    list_display = ('name', 'forum_type', 'forum')
#    list_filter = ('forum_type', 'issubforum')

admin.site.register(Stock)                                  # shows the Stock that are created in the admin page
admin.site.register(Purchases)                              # shows the Purchases that are created in the admin page