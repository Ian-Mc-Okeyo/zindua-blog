from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "John Doe",
        "title": "Django",
        "date_posted": "Aug 22 2024",
        "content":"Django is nice"
    },
    {
        "author": "Jane Doe",
        "title": "React",
        "date_posted": "Aug 22 2024",
        "content":"React is nice"
    },
    {
        "author": "Dan Doe",
        "date_posted": "Aug 22 2024",
        "content":"Java is nice"
    }
]
def home(requests):
    print("Hello, this is the home page")
    context = {
        "posts": posts,
        "title": "Blog Post"
    }
    return render(requests, "blog/home.html", context)

def about(requests):
    return render(requests, "blog/about.html")

def contactUs(requests):
    return render(requests, "blog/contact.html")