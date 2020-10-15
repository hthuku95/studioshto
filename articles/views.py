from django.shortcuts import render,redirect
from .models import Contact ,Article,Comment,Category,Reply
from .forms import CommentForm , ReplyForm


# Create your views here.

#article list page
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/article_list.htm',{'articles':articles})

#article details
def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(parent_article=article)
    #updating the number of views
    article.views = article.views + 1
    article.save()
    
    #forms
    form = CommentForm()
    form_2 = ReplyForm()

    #number of comments
    numberOfComments = Comment.objects.filter(parent_article=article).count()
    return render(request,'articles/article_details.htm',{'article':article,'comments':comments,'form':form,'form_2':form_2,'numberOfComments':numberOfComments})


#article comments
def article_comment(request,slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            #getting values of the form field
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            comment_body = form.cleaned_data['comment']

            newComment = Comment(name = name,parent_article = article,comment_body = comment_body, email=email_address)
            newComment.save()
    return redirect('/articles/'+article.slug+ '/')

#article reply
def article_reply(request,slug):
    article = Article.objects.get(slug=slug)
    comment = Comment.objects.get(parent_comment=parent_comment)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            #getting values of the form field
            name = form.cleaned_data['name']
            email_address = form.cleaned_data['email']
            reply_body = form.cleaned_data['reply']

            newReply = Reply(name = name,parent_comment = comment,reply_body = reply_body, email=email_address)
            newReply.save()
    return redirect('/articles/'+article.slug+ '/')

