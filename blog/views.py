from django.shortcuts import render

posts = [
    {
        'author': 'SandyC',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Today'
    },
    {
        'author': 'molly',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'yesterday'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
