from django.shortcuts import render
from .models import BuildSection


def build_sections(request):
    build_sections = BuildSection.objects.all()
    return render(request, 'build/build_sections.html', {'build_sections': build_sections})


def build_section_detail(request, pk):
    build_section = BuildSection.objects.get(pk=pk)
    builds = build_section.build_set.all()
    return render(request, 'build/build_section_detail.html', {'build_section': build_section, 'builds': builds})
