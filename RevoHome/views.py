from django.shortcuts import render, redirect
from .models import BuildSection
from .forms import AmountMadeForm


def build_sections(request):
    build_sections = BuildSection.objects.all()
    return render(request, 'build/build_sections.html', {'build_sections': build_sections})


def build_section_detail(request, pk):
    build_section = BuildSection.objects.get(pk=pk)
    builds = build_section.build_set.all()
    if request.method == 'POST':
        form = AmountMadeForm(request.POST)
        if form.is_valid():
            amount_made = form.save(commit=False)
            amount_made.build_section = build_section
            amount_made.save()
            return redirect('build_section_detail', pk=pk)
    else:
        form = AmountMadeForm()
    return render(request, 'build/build_section_detail.html', {'form': form, 'build_section': build_section, 'builds': builds})
