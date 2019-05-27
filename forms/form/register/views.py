from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Subscription
from .forms import SubscriptionForm
# Create your views here.


def home(request):
    return render(request, 'index.html')


class Create(CreateView):
    template_name = 'register.html'
    form_class = SubscriptionForm
    success_url = reverse_lazy('list')


class List(ListView):
    template_name = 'list.html'
    form_class = SubscriptionForm
    context_object_name = 'name'

    def get_queryset(self):
        return Subscription.objects.order_by('-made_in')

