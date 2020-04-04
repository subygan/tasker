from django.contrib import admin
from .models import Profile, Task


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'created_on')
    search_fields = ['title', 'content']


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'created_on')
    search_fields = ['title', 'description']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Task, TaskAdmin)
