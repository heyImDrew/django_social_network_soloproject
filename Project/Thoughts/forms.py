from django import forms

class PostForm(forms.Form):
    text = forms.CharField(label='Post', max_length=255)

class CommentForm(forms.Form):
    text = forms.CharField(label='Comment', max_length=255)