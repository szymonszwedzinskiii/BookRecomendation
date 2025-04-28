from django.shortcuts import render
from .models import Book
from .forms import GenreForm

def recommend_books(request):
    books = None
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            books = Book.objects.filter(genre__icontains=genre)
    else:
        form = GenreForm()

    return render(request, 'recommend.html', {'form': form, 'books': books})