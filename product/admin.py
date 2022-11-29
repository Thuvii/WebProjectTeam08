from django.contrib import admin

from product.models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'best_seller_course')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'course_status',
                    'instructor', 'lesson_number', 'course_status', 'rated', 'image', 'duration', 'slug')

    prepopulated_fields = {'slug': ('title', )}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
