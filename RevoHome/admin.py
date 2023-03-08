from django.contrib import admin
from django.db.models import Sum
from django.forms import inlineformset_factory
from .models import BuildSection, Build, BuildPart, AmountMade


class BuildPartInline(admin.TabularInline):
    model = BuildPart
    extra = 1


class BuildAdmin(admin.ModelAdmin):
    inlines = [BuildPartInline]


class AmountMadeAdmin(admin.ModelAdmin):
    readonly_fields = ('build_section', 'amount_made', 'created_at')

    def has_add_permission(self, request, obj=None):
        return False

    def total_amount_made(self, obj):
        total = AmountMade.objects.aggregate(Sum('amount_made'))[
            'amount_made__sum']
        return total

    total_amount_made.short_description = 'Total Amount Made'

    list_display = ('build_section', 'amount_made',
                    'created_at', 'total_amount_made')


admin.site.register(BuildSection)
admin.site.register(Build, BuildAdmin)
admin.site.register(AmountMade, AmountMadeAdmin)
