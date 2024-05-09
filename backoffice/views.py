from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('review_container')
        stars = request.POST.get('rating')
        
        if stars is not None:
            stars = int(stars)
        else:
            stars = 0  
        
        review = Review.objects.create(author=author, content=content, rating=stars)
        return redirect('index')
    
    else:
        slides = Slide.objects.all()
        homesections = HomeSection.objects.all()
        books = Book.objects.all()
        novelties = Noveltie.objects.all()
        announcements = Announcement.objects.all()
        reviews = Review.objects.all()
        
        return render(request, 'website/index.html', {
            "slides": slides,
            "homesections": homesections,
            'books': books,
            "novelties": novelties,
            "announcements": announcements,
            "reviews": reviews
        })

