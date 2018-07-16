from django import forms

from .models import News,Images


class CreateNews(forms.ModelForm):


    class Meta:
        model = News
        fields = ('title','slug','image','image_url','user','content','created','update')


