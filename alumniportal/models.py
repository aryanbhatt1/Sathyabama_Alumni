from django.db import models
from django.conf import settings
"""
"""
class Gender(models.Model):
    gender = models.CharField("Gender", max_length=20, null=True)

    def __str__(self):
        return self.gender


class Degree(models.Model):
    Degree = models.CharField("Degree", max_length=200, null=True)

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
        return "{} - {}".format(self.year1, self.year2)


class Overview(models.Model):
    total_text = models.CharField(max_length=30, null=True)
    total = models.IntegerField('Total', null=True)

    def __str__(self):
        return self.total_text


class Events(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user_name = models.CharField('User First Name', max_length=50, null=True)
    last_name = models.CharField('User Last Name', max_length=50, null=True)
    title = models.CharField('Title', max_length=100, null=True)
    date = models.DateField('Date', null=True)
    time = models.TimeField('Time', null=True)
    venue = models.CharField('Venue', max_length=50, null=True)
    description = models.TextField('Description', null=True)
    poster = models.ImageField('Poster', upload_to='Events/', null=True)
    photo = models.ImageField('Photo', null=True)
    date_time_upload = models.DateTimeField(null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = 'Events'

class PresentStatus(models.Model):
    status = models.CharField('Status', max_length=50, null=True)

    def __str__(self):
        return self.status
class FacultyUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    profile_image = models.ImageField('Profile Photo', upload_to='profile_image', null=True)
    first_name = models.CharField('First Name', max_length=50, null=True)
    last_name = models.CharField('Last Name', max_length=50, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    YearOfCompletion = models.ForeignKey(YearOfCompletion, on_delete=models.CASCADE, null=True)
    EmploymentType = models.ForeignKey(EmploymentType, on_delete=models.CASCADE, null=True)
    present_employer_name = models.CharField('Present Employer Name', max_length=50, blank=True, null=True)
    designation = models.CharField('Designation', max_length=50, blank=True, null=True)
    country = models.CharField('Country', max_length=80, blank=True, null=True)
    state = models.CharField('State', max_length=90, blank=True, null=True)
    city = models.CharField('City', max_length=90, blank=True, null=True)
    special_achievement = models.TextField('Special Achievement', blank=True, null=True)
    present_status = models.ForeignKey(PresentStatus, on_delete=models.CASCADE, blank=True, null=True)
    university_name = models.CharField('University Name', max_length=100, blank=True, null=True)
    country_university = models.CharField('Country', max_length=100, blank=True, null=True)
    state_university = models.CharField('State', max_length=100, blank=True, null=True)
    city_university = models.CharField('City', max_length=100, blank=True, null=True)
    country_current = models.CharField('Country', max_length=100, null=True)
    state_current = models.CharField('State', max_length=100, null=True)
    city_current= models.CharField('City', max_length=100, null=True)
    phone1 = models.IntegerField('Phone 1 (Office)', blank=True, null=True)
    phone2 = models.IntegerField('Phone 2 (Residence)', blank=True, null=True)
    mobile = models.CharField('Mobile', max_length=20, null=True)
    email_id = models.EmailField('Email', null=True)
