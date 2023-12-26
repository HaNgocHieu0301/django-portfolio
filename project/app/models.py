from django.contrib.auth.models import User
from django.db import models
from rich.markup import Tag


# Create your models here.
class UserInfo(User):
    middle_name = models.CharField('middle name', max_length=50, blank=True, null=True)
    dob = models.DateField()
    phone = models.CharField(max_length=11)
    introduction = models.TextField()
    position = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='static/images/', blank=True, null=True)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)
    facebook_link = models.CharField(max_length=100, blank=True, null=True)
    linkedin_link = models.CharField(max_length=100, blank=True, null=True)
    github_link = models.CharField(max_length=100, blank=True, null=True)
    twitter_link = models.CharField(max_length=100, blank=True, null=True)

    def get_full_name(self):
        if self.middle_name:
            return "%s %s %s" % (self.last_name, self.middle_name, self.first_name)
        return "%s %s" % (self.last_name, self.first_name)

    def get_short_introduction(self):
        return "Hi, My name is %s. I'm a %s" % (self.get_full_name(), self.position)


class Skill(models.Model):
    title = models.CharField(max_length=200)
    img_url = models.ImageField(upload_to='static/images/', blank=True)
    description = models.TextField()
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='skills')


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)


class Project(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    img_url = models.ImageField(upload_to='static/images/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    # tags = models.ManyToManyField(Tag, through='ProjectTag', blank=True)

# class ProjectTag(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('project', 'tag')


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()