from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from webapp.models import Tracker, Type, Status
from webapp.forms import TrackerForm, TypeForm, StatusForm

class TypeView(ListView):
    context_object_name = 'types'
    model = Type
    template_name = 'types_ls.html'

def types_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TypeForm()
        return render(request, 'create_type.html', context={'form': form})
    elif request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(type=form.cleaned_data['type'])
            return redirect('type_ls')
        else:
            return render(request, 'create_type.html', context={'form': form})

def types_edit_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        form = TypeForm(data={'type' : type.type})
        return render(request, 'update_type.html', context={'form': form, 'type': type})
    elif request.method == 'POST':
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.type = request.POST.get('type')
            type.save()
            return redirect('type_ls')
        else:
            return render(request, 'update_type.html', context={'type': type, 'form': form})
    return redirect('type_ls')

def type_delete_view(request, pk):
    type = get_object_or_404(Type, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_type.html', context={'type': type})
    elif request.method == 'POST':
        type.delete()
        return redirect('type_ls')