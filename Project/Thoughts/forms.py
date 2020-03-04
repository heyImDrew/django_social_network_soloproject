from django import forms

class PostForm(forms.Form):
    text = forms.CharField(label='Post', max_length=255)