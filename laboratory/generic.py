'''
Created on 11/8/2016

@author: natalia
'''
from __future__ import unicode_literals

from django.views.generic.edit import CreateView, DeleteView
from laboratory.models import Shelf, Object, LaboratoryRoom
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.db.models.query import QuerySet
from django_ajax.mixin import AJAXMixin


class ObjectDeleteFromShelf(DeleteView):
    model = Object
    success_url = reverse_lazy('laboratory:object-list')


class ObjectList(ListView):
    model = Object


class LaboratoryRoomsList(ListView):
    model = LaboratoryRoom


class LabroomCreate(CreateView):
    model = LaboratoryRoom
    fields = '__all__'
    success_url = reverse_lazy('laboratory:object-list')


class ObjectCreate(CreateView):
    model = Object
    fields = '__all__'
    success_url = "/"


class ShelfCreate(AJAXMixin, CreateView):
    model = Shelf
    fields = '__all__'
    success_url = "/"


class ShelfDelete(DeleteView):
    model = Shelf
    success_url = reverse_lazy('laboratory:object-list')


class LabRoomList(ListView):
    model = LaboratoryRoom


class ShelfListView(ListView):
    model = Shelf

    def get_queryset(self):
        queryset = ListView.get_queryset(self)
        queryset = queryset.filter(container_shelf__gte=5)
        return queryset
