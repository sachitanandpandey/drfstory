from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


from django.template.defaultfilters import slugify
import feedparser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


import math

MOTIVATION_LIST = [
    'Time to start writing',
    'You\'ve barely started!',
    'Time to get writing?',
    'You\'re getting somewhere now',
    'Nearly halfway there!',
    'The midway point',
    'It\'s all downhill from here',
    'Three quarters of the way there',
    'Almost at the finish',
    'Last push and you\'ll be done',
    'You\'ve done it!'
];


class Genre(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    storyslug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=256, help_text="Short and snappy? Verbose yet informative?")
    author = models.CharField(max_length=128, help_text="A pseudonym? Remember, you can always change this later")
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name="reviewer")

    def save(self, *args, **kwargs):
        uniquestring = "%s %s" % (self.title, self.author)
        self.storyslug = slugify(uniquestring)
        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, related_name='chapter', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    weight = models.IntegerField(default=1)
    content = models.TextField(null=True, blank=True)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="chp_reviewer")

    def __str__(self):
        return self.title


@receiver(post_save, sender=Story)
def post_save_create_profile(sender, instance, created, **kwargs):
    print("****************************************************")
    print(instance.reviewer)
    print("****************************************************")
    Chapter.objects.update(reviewer=instance.reviewer)