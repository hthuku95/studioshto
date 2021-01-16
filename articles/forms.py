from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))

class ReplyForm(forms.Form):
    reply = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))


