from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=40)


class DailyKnown(models.Model):

    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=300)
    tag = models.ForeignKey(Tags, on_delete=models.PROTECT, 
                            related_name='Days', null=True, blank=True)

    class Meta:
        verbose_name = _("DailyKnown")
        verbose_name_plural = _("DailyKnowns")

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"    

class Topic(models.Model):
    text = models.CharField(max_length=1000)
    day = models.ForeignKey(DailyKnown, on_delete=models.PROTECT, related_name='topics')
