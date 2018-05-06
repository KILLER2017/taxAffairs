from django.contrib import admin
from .models import List, ListItem
# Register your models here.


class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 3


class ListAdmin(admin.ModelAdmin):
    '''
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    '''
    inlines = [ListItemInline]


admin.site.register(List, ListAdmin)