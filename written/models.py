from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class DailyKnown(models.Model):

    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = _("DailyKnown")
        verbose_name_plural = _("DailyKnowns")

    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"
