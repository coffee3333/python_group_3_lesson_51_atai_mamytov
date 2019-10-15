from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm, TypeForm, StatusForm



def status_list(request, *args, **kwargs):
    statuses = Status.objects.all()
    return render(request, 'status_ls.html', context={'statuses': statuses})


def statuses_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = StatusForm()
        return render(request, 'create_status.html', context={'form': form})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(type=form.cleaned_data['status'])
            return redirect('status_ls')
        else:
            return render(request, 'create_status.html', context={'form': form})


def statuses_edit_view(request, pk):
    statuses = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        form = StatusForm(data={'status' : statuses.status})
        return render(request, 'update_status.html', context={'form': form, 'status': statuses})
    elif request.method == 'POST':
        form = StatusForm(data=request.POST)
        if form.is_valid():
            statuses.status = request.POST.get('status')
            statuses.save()
            return redirect('status_ls')
        else:
            return render(request, 'update_status.html', context={'status': statuses, 'form': form})
    return redirect('status_ls')


def statuses_delete_view(request, pk):
    statuses = get_object_or_404(Status, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_status.html', context={'status': statuses})
    elif request.method == 'POST':
        statuses.delete()
        return redirect('status_ls')