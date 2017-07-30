from django.shortcuts import render

from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)

from django.core.urlresolvers import reverse
from django.views import generic

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields: ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
