from django import forms
from written.models import Topic

class TopicForms(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        models = Topic
    
