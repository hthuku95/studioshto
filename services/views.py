from django.shortcuts import render , redirect

# Create your views here.

def services_view(request):
    return redirect(request,'/')

def animation_view(request):
    return render(request,'services/animation_view.htm')
    
def app_view(request):
    return render(request,'services/app_view.htm')

def art_view(request):
    return render(request,'services/art_view.htm')

def threed_view(request):
    return render(request,'services/threed_view.htm')

def web_view(request):
    return render(request, 'services/web_view.htm')

def game_view(request):
    return render(request, 'services/game_view.htm')