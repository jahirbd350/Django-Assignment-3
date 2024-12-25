from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        fields = '__all__'
