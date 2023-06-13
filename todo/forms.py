from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        max_length=80,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Yeni tapşırıq"}),
        required=True,
    )

    class Meta:
        model = Todo
        fields = ["title"]
        labels = {
            "title": "Todo Başlığı"
        }


class TodoDetailForm(forms.ModelForm):
    title = forms.CharField(
        max_length=80,
        widget=forms.TextInput(
            attrs={"class": "form-control"}),
        required=True,
        label="Todo Başlığı"
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control"}),
        required=False,
        label="Açıqlama"
    )

    class Meta:
        model = Todo
        fields = ["title", "description"]
