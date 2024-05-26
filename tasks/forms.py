from django import forms
from tasks.models import Task, Comment
from django.forms import TextInput, FileInput, DateTimeInput, Textarea, Select

class TaskForm(forms.ModelForm):
    class Meta:
        STATUS_CHOICES = [
            ["", "All"],
            ["to_do", "To Do"],
            ["in_progress", "In Progress"],
            ["done", "Done"],
        ]
        model = Task
        fields = ["title", "description", "status", "priority", "due_date", "creator"]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'description': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Description'
                }),
            'status': Select(attrs={
                'class': "form-select",
                'style': 'max-width: 300px;',
                }),
            'priority': Select(attrs={
                'class': "form-select",
                'style': 'max-width: 300px;',
                }),
            'due_date': DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Due date'
                }),
            
        }
        
class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ["", "All"],
        ["to_do", "To Do"],
        ["in_progress", "In Progress"],
        ["done", "Done"],
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label='status')
    
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content', 'media']
        widgets = {
            'media': FileInput()
        }