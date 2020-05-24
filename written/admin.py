from django.contrib import admin
from django.db import models
from django import forms
from written.models import DailyKnown, Topic, Tags
from written.forms import TopicForms
class TopicsAdmin(admin.TabularInline):
    model = Topic
    formfield_overrides = {
                models.TextField: {
                    'widget': forms.Textarea(attrs={
                        'rows': 20,
                        'cols': 40})},

    }

# Register your models here.
@admin.register(DailyKnown)
class DailyKnownAdmin(admin.ModelAdmin):
    inlines = [
        TopicsAdmin
    ]
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(
                                       attrs={'rows': 1,
                                                                                'cols': 40,
                                                                                'style': 'height: 1em;'}
        )},
    }


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
