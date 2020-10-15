from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    comment = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))

class ReplyForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    reply = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))
