from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskCompleteForm, TaskForm
from tasks.models import Task, Tag


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


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
