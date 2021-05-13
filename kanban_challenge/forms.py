from django import forms
from .models import TicketCard
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class TicketCardForm(forms.ModelForm):
  content = forms.CharField(label='contnt', required=True)
  post_people = forms.CharField(label='Name', required=True)

# このMetaの中身というのはmodelsのフィールドを元にしている
  class Meta:
      model = TicketCard
      fields = [
          'content',
          'post_people',
      ]
