from django.shortcuts import render
from .models import Experience, Project, Skill

def home(request):
    experiences = Experience.objects.all()[:4]  # Top 4 experiences
    projects = Project.objects.filter(featured=True)[:6]  # Featured projects
    skills = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'experiences': experiences,
        'projects': projects,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def contact(request):
    return render(request, 'main/contact.html')

