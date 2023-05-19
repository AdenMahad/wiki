from django import forms


class NewEntry(forms.Form):
    title = forms.CharField(max_length=50,label="title",required= True)
    content = forms.CharField(label="content",widget=forms.Textarea(attrs={'rows':2, 'cols':3}))
