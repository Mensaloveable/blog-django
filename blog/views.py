from django.shortcuts import render

posts = [
    {
        'author': 'Mensa',
        'title': 'Love',
        'content': 'How to be loveabe',
        'date': 'August 27 2023'
    },
    {
        'author': 'Loveable',
        'title': 'Mensa',
        'content': 'How to be a king',
        'date': 'August 18 2023'
    },
    {
        'author': 'Great',
        'title': 'Mensa',
        'content': 'How to be a king'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# /Users/decagon/Desktop/dev/Django/django_project/blog/template/blog/home.html
