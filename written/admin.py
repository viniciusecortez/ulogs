from django.contrib import admin
from written.models import DailyKnown, Topic, Tags
from written.forms import TopicForms
class TopicsAdmin(admin.TabularInline):
    model = Topic
    form = TopicForms

# Register your models here.
@admin.register(DailyKnown)
class DailyKnownAdmin(admin.ModelAdmin):
    inlines = [
        TopicsAdmin
     ]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
