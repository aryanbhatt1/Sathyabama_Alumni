from django.db import models


class Degree(models.Model):
    Degree = models.CharField("Degree", max_length=50, null=True)

    def __str__(self):
        return self.Degree


class EmploymentType(models.Model):
    EmploymentType = models.CharField("Employment Type", max_length=30, null=True)

    def __str__(self):
        return self.EmploymentType


class YearOfCompletion(models.Model):
    year1 = models.CharField("Year 1", max_length=20, null=True)
    year2 = models.CharField("Year 2", max_length=20, null=True)

    def __str__(self):
        return "%s - %s".format(self.year1, self.year2)


class Overview(models.Model):
    total_text = models.CharField(max_length=30, null=True)
    total = models.IntegerField('Total', null=True)

    def __str__(self):
        return self.total_text


class Events(models.Model):
    title = models.CharField('Title', max_length=100, null=True)
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    venue = models.CharField('Venue', max_length=50, null=True)
    description = models.TextField('Description', null=True)
    poster = models.ImageField('Poster', upload_to='Events/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = 'Events'

