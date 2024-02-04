from main.models import Commentary
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['name', 'message', 'email', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "",

        })

        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "",

        })

        self.fields['email'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "",

        })

        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "",

        })
