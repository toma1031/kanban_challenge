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
    context['form'] = TicketCardForm # ←こちらを追加
    return context

# TemplateViewはdef form_valid() を持っていないので
# def post() 側で処理を書いてあげる必要がある
  def post(self, request, **kwargs):
        form = TicketCardForm(request.POST)
        if form.is_valid():
          print(request.POST)
          form.save()
          return redirect('kanban_challenge:index')