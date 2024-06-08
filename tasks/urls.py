from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="task-list"),
    path('<int:pk>/', views.TaskDetailView.as_view(), name="task-detail"),
    path('task-create', views.TaskCreateView.as_view(), name="task-create"),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name="task-update"),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name="task-delete"),
    path('comment/like/<int:pk>', views.CommentLikeToggle.as_view(), name="comment-like-toggle"),
    path('comment/update/<int:pk>', views.CommentUpdateView.as_view(), name="comment-update"),
    path('comment/delete/<int:pk>', views.CommentUpdateView.as_view(), name="comment-delete"),
]

app_name = "tasks"