from django.contrib import admin
from .models import Experience, Project, Skill

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['title', 'company']
    ordering = ['-order', '-start_date']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order']
    list_filter = ['featured']
    search_fields = ['title', 'description']
    ordering = ['-featured', '-order']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category', 'proficiency']
    search_fields = ['name']
    ordering = ['category', '-proficiency']

