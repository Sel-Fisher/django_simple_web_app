from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    technologies_required = models.ManyToManyField(Technology, related_name="vacancy")
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.company_name})"
