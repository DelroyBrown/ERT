from django.db import models


class BuildSection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class BuildPart(models.Model):
    build = models.ForeignKey('Build', on_delete=models.CASCADE, related_name='parts')
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
