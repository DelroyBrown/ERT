from django.db import models
from django.db.models import Sum


class BuildSection(models.Model):
    name = models.CharField(max_length=100)

    # @property
    # def total_amount_made(self):
    #     return self.amounts.filter(created_at__date=self.created_at.date()).aggregate(Sum('amount_made'))['amount_made__sum'] or 0

    def __str__(self):
        return self.name


class BuildPart(models.Model):
    build = models.ForeignKey(
        'Build', on_delete=models.CASCADE, related_name='parts')
    name = models.CharField(max_length=100, default='')
    length = models.FloatField(blank=True, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Build(models.Model):
    build_section = models.ForeignKey(BuildSection, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)

    def __str__(self):
        return self.build_section.name


class AmountMade(models.Model):
    build_section = models.ForeignKey(
        BuildSection, related_name='amounts', on_delete=models.CASCADE)
    amount_made = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('build_section', 'created_at')

    def __str__(self):
        return f'{self.build_section.name} - {self.created_at.strftime("%Y-%m-%d")}: {self.amount_made}'
    
    @property
    def total_amount_made(self):
        return self.amounts.filter(created_at__date=self.created_at.date()).aggregate(Sum('amount_made'))['amount_made__sum'] or 0


