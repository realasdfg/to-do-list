from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from tasks.forms import TaskCompleteForm
from tasks.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    queryset = Task.objects.prefetch_related("tags")

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id)
        form = TaskCompleteForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("tasks:index")
