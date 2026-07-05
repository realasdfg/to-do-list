from django import forms

from tasks.models import Task


class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("is_done",)
