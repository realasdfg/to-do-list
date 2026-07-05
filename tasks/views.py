from django.views import generic

from tasks.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    queryset = Task.objects.prefetch_related("tags")
