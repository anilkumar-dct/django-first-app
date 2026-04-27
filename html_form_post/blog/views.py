from django.shortcuts import render
from  .models import Post

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return result(request)
    return render(request, 'home.html')

def result(request):
    posts = Post.objects.all()
    return render(request, 'result.html', {'posts': posts})