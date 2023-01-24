from django.shortcuts import render, get_object_or_404
from mangaApp.models import Series, Tome, Chapter


def home(request):
    return render(request, 'mangaApp/home.html')


# Partie Serie

def series_list(request):
    series_list = Series.objects.all()
    context = {'series_list': series_list}
    return render(request, 'mangaApp/series_list.html', context)


def series_detail(request, series_id):
    series = Series.objects.get(pk=series_id)
    tomes = Tome.objects.filter(series=series)
    context = {'series': series, 'tomes': tomes}
    return render(request, 'mangaApp/series_detail.html', context)


# Partie Tome :

def tome_list(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    tomes = Tome.objects.filter(series=series)
    context = {'series': series, 'tomes': tomes}
    return render(request, 'mangaApp/tome_list.html', context)


def tome_detail(request, tome_id):
    tome = Tome.objects.get(pk=tome_id)
    chapters = Chapter.objects.filter(tome=tome)
    context = {'tome': tome, 'chapters': chapters}
    return render(request, 'mangaApp/tome_detail.html', context)


# Partie Chapitre :

def chapter_list(request):
    chapter_list = Chapter.objects.all()
    context = {'chapter_list': chapter_list}
    return render(request, 'mangaApp/chapter_list.html', context)


def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)
    context = {'chapter': chapter}
    return render(request, 'mangaApp/chapter_detail.html', context)
