from django.urls import path

from tasks.views import (
    IndexView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "tasks"
