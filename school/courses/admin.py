from django.contrib import admin

from .models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'category', 'duration', 'description'
    )
    list_display_links = ('name',)

    def text_short(self, obj):
        if len(obj.description) < 40:
            return obj.description
        return f'{obj.description[:40]}...'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'course', 'date', 'duration', 'description'
    )
    list_display_links = ('name',)

    def text_short(self, obj):
        if len(obj.description) < 40:
            return obj.description
        return f'{obj.description[:40]}...'
