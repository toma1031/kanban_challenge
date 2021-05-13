from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .models import TicketCard
from .forms import TicketCardForm
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
  # TemplateViewの場合はモデルの表記はいらない
  template_name = "index.html"
  context_object_name = 'ticketcard_list'
  form_class = TicketCardForm
  success_url = reverse_lazy('index')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # backlogsというkeyに対して、status=1のTicketCardのオブジェクトをvalueとして入れ込んでいる
    context['backlogs']= TicketCard.objects.filter(status=1)
    context['progress'] = TicketCard.objects.filter(status=2)
    context['completes'] = TicketCard.objects.filter(status=3)
    return context

  # def form_valid(self, form):
  #   form = form.save(commit=False)
  #   form.save()
  #   return redirect('index')