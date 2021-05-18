from typing import ContextManager, no_type_check
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
    # contextという変数にTemplateView（ここではsuperがTemplateViewを表している）のContextデータをGetして辞書型として代入
    # この時点で変数contextにはticketcard_listが辞書型で入っている。
    context = super().get_context_data(**kwargs)
    # １、つまりcontextには？？？が入っている。Printすると？？？と出てくる
    print(context)
    # backlogsというkeyに対して、status=1のTicketCardのオブジェクトをvalueとして入れ込んでいる
    context['backlogs']= TicketCard.objects.filter(status=1)
    context['progress'] = TicketCard.objects.filter(status=2)
    context['completes'] = TicketCard.objects.filter(status=3)
    # ２、これはなぜ必要なか？
    context['form'] = TicketCardForm # ←こちらを追加
    return context

# TemplateViewはdef form_valid() を持っていないので
# def post() 側で処理を書いてあげる必要がある
  def post(self, request, **kwargs):
# もしTicketCardのステータスが１なら
    if self.request.POST.get('data-id', None):
      update2 = TicketCard.objects.filter(id=self.request.POST.get('data-id')).update(status=self.request.POST.get('status-id'))
      print(update2)
      print('B')
    else:
      print('A')
      form = TicketCardForm(request.POST)
      if form.is_valid():
        form.save()
    return redirect('kanban_challenge:index')