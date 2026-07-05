from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from task.models import Task, Tag, User

admin.site.unregister(Group)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "deadline", "created_at", "is_done",)
    list_filter = ("deadline", "created_at", "is_done",)
    search_fields = ("content",)


@admin.register(Tag)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(User, UserAdmin)
