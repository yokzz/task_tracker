from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Task(models.Model):
    
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
    
    title = models.CharField(max_length=63)
    description = models.TextField()
    status = models.CharField(max_length=31, choices=STATUS_CHOICES, default="to_do")
    priority = models.CharField(max_length=31, choices=PRIORITY_CHOICES, default="medium")
    due_date = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:task-detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments_media/", blank=True, null=True)

    def get_absolute_url(self):
        return self.task.get_absolute_url()
    

class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user') 