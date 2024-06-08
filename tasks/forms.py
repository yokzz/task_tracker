from django import forms
from tasks.models import Task, Comment
from django.forms import TextInput, FileInput, DateTimeInput, Textarea, RadioSelect

STATUS_CHOICES = [
        ["to_do", "To Do"],
        ["in_progress", "In Progress"],
        ["done", "Done"],
    ]
    
PRIORITY_CHOICES = [
            ["low", "Low"],
            ["medium", "Medium"],
            ["high", "High"],
            ["cricital", "Cricital"]
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]
    
    title = forms.CharField(
            label='Title',
            widget=forms.TextInput(
                attrs = {
                    'class': "form-control rounded-3",
                    'id': "title",
                    'placeholder': 'Title',
                    'style': 'max-width: 300px;'
                }
            )
        )
        
    description = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                'class': "form-control rounded-3",
                'id': "description",
                'placeholder': 'Description',
                'style': 'max-width: 300px;'
            }
        )
    )
    
    status = forms.CharField(
        label='Status',
        widget=forms.Select(
            attrs = {
                'class': "form-control rounded-3",
                'id': "status",
                'placeholder': 'Status',
                'style': 'max-width: 300px;'
            },
            choices=STATUS_CHOICES
        )
    )
    
    priority = forms.CharField(
        label='Priority',
        widget=forms.Select(
            attrs = {
                'class': "form-control rounded-3",
                'id': "priority",
                'placeholder': 'Priority',
                'style': 'max-width: 300px;'
            },
            choices=PRIORITY_CHOICES
        )
    )
    
    due_date = forms.DateTimeField(
        label='Due Date',
        widget=forms.DateTimeInput(
            attrs = {
                'class': "form-control rounded-3",
                'id': "due_date",
                'placeholder': 'Due Date',
                'style': 'max-width: 300px;',
                'type': 'datetime-local'
            }
        )
    )
        
class TaskFilterForm(forms.Form):
            
    STATUS_CHOICES = [
        ["", "All"],
        ["user_owner", "My tasks"]
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)
    
    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "form-control"})
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content', 'media']
        
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs = {
                'class': "form-control rounded-3",
                'id': "content",
                'placeholder': 'Content',
                'style': 'max-width: 300px;'
            },
        )
    )
    
    media = forms.FileField(
        label = 'Media',
        widget = forms.FileInput(
            attrs={
                'msg cols': '30',
                'rows': '5',
                'class': 'form-control',
                'style': 'border: 1px solid #4c486b;',
                'label': 'Media'
            },
        )
    )