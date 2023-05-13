from django import forms


class NewEntry(forms.Form):
    title = forms.CharField(max_length=50,label="title")
    content = forms.CharField(label="content",widget=forms.Textarea(attrs={"size":"20"}))