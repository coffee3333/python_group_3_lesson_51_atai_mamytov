from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, ListView

from webapp.models import Tracker
from webapp.forms import TrackerForm
from webapp.views.detail_view import DetailView


class IndexView(ListView):
    context_object_name = 'trackers'
    model = Tracker
    template_name = 'index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

class TaskTrackerView(DetailView):
    template_name = 'TaskTrack.html'
    context_key = 'tracker'
    model = Tracker
    key_kwarg = 'pk'


class TaskTrackerCraeteView(View):
    def get(self, request, *args, **kwargs):
        form = TrackerForm()
        context = {
            'form': form
        }
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            Tracker.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


class TaskTrackerUpdateView(View):
    def get(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        form = TrackerForm(data = {
            'summary':task_tracker.summary,
            'description':task_tracker.description,
            'status':task_tracker.status,
            'type':task_tracker.type
        })
        context = {
            'task_tracker': task_tracker,
            'form': form
        }
        return render(request, 'update.html', context)

    def post(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            task_tracker.summary = request.POST.get('summary')
            task_tracker.description = request.POST.get('description')
            task_tracker.Status = request.POST.get('status')
            task_tracker.Type = request.POST.get('type')
            task_tracker.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'task_tracker': task_tracker, 'form': form})

    def get_odject(self, pk):
        task_tracker = get_object_or_404(Tracker, pk = pk)
        return task_tracker


class TaskTrackerDeleteView(View):
    def get(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        context = {'task_tracker': task_tracker}
        return render(request, 'delete.html', context)

    def post(self, request, *args, **kwargs):
        task_tracker = self.get_odject(self.kwargs.get('pk'))
        task_tracker.delete()
        return redirect('index')

    def get_odject(self, pk):
        task_tracker = get_object_or_404(Tracker, pk = pk)
        return task_tracker



