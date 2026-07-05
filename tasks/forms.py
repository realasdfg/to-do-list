from django import forms

from tasks.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags",)


class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("is_done",)
