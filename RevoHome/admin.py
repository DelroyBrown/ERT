from django.contrib import admin
from django.forms import inlineformset_factory
from .models import BuildSection, Build, BuildPart

class BuildPartInline(admin.TabularInline):
    model = BuildPart
    extra = 1

class BuildAdmin(admin.ModelAdmin):
    inlines = [BuildPartInline]

admin.site.register(BuildSection)
admin.site.register(Build, BuildAdmin)
