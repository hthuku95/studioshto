from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from .models import Contact ,Article,Comment,Category,Reply
from .forms import CommentForm , ReplyForm


# Create your views here.

#article category page
def article_category(request, slug):
    articles = Article.objects.filter(category__name = slug)
    categories = Category.objects.all()
    return render(request,'articles/article_category.htm',{'articles':articles,'categories':categories})

#article list page
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request,'articles/article_list.htm',{'articles':articles})

#article details
def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    stories = Article.objects.all().order_by('date')[:5]
    comments = Comment.objects.filter(parent_article=article)
    #updating the number of views
    article.views = article.views + 1
    article.save()
    
    #forms
    form = CommentForm()
    form_2 = ReplyForm()

    #number of comments
    numberOfComments = Comment.objects.filter(parent_article=article).count()
    return render(request,'articles/article_details.htm',{'article':article,'comments':comments,'form':form,'form_2':form_2,'numberOfComments':numberOfComments,'stories':stories})


#article comments
@login_required(login_url= "/accounts/login")
def article_comment(request,slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        User = get_user(request)
        form = CommentForm(request.POST)
        if form.is_valid():

            #getting values of the form field
            comment_body = form.cleaned_data['comment']

            newComment = Comment(user = User,parent_article = article,comment_body = comment_body)
            newComment.save()
    return redirect('/articles/'+article.slug+ '/')

#article reply
def article_reply(request,slug):
    article = Article.objects.get(slug=slug)
    comment = Comment.objects.get(parent_comment=parent_comment)
    if request.method == 'POST':
        User = get_user(request)
        form = ReplyForm(request.POST)
        if form.is_valid():

            #getting values of the form field
            reply_body = form.cleaned_data['reply']

            newReply = Reply(user = User,parent_comment = comment,reply_body = reply_body)
            newReply.save()
    return redirect('/articles/'+article.slug+ '/')

