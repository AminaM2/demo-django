from django.shortcuts import render
from .forms import PollForm
from .models import Poll

from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView
)

# Create your views here.
class PollListView(ListView):
    template_name = 'polls/poll_list.html'
    queryset      = Poll.objects.filter(is_active=True).all()
    model         = Poll

class PollDetailView(DetailView):
    template_name = 'polls/poll_detail.html'
    queryset      = Poll.objects.filter(is_active=True).all()
    model         = Poll

class PollCreateView(CreateView):
    template_name = 'polls/poll_create.html'
    form_class    = PollForm
    model         = Poll

# ex of other methods that we can override: setup, dispatch,get_queryset, get_context_data(), get(), render_to_response()
# def get_queryset(self):
#        queryset = super(PhotoDetail, self).get_queryset()
#        return queryset.filter(photoextended__user=self.request.user)