"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskTrackerView, TaskTrackerCraeteView, TaskTrackerUpdateView, TaskTrackerDeleteView, \
    types_list, status_list, types_create_view, statuses_create_view, types_edit_view, statuses_edit_view, type_delete_view, statuses_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('track/<int:pk>/', TaskTrackerView.as_view(), name='task_track'),
    path('track/add/', TaskTrackerCraeteView.as_view(), name='task_track_add'),
    path('track/<int:pk>/edit', TaskTrackerUpdateView.as_view(), name='task_track_edit' ),
    path('track/<int:pk>/delete', TaskTrackerDeleteView.as_view(), name='task_track_delete'),
    path('types/', types_list, name='type_ls'),
    path('statuses/', status_list, name='status_ls'),
    path('types/create/', types_create_view, name='type_create'),
    path('statuses/create/', statuses_create_view, name='status_create'),
    path('types/edit/<int:pk>', types_edit_view, name='type_edit'),
    path('statuses/edit/<int:pk>', statuses_edit_view, name='status_edit'),
    path('types/delete/<int:pk>', type_delete_view, name='type_delete'),
    path('statuses/delete/<int:pk>', statuses_delete_view, name='status_delete')
]
