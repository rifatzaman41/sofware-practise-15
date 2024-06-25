from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from music_app1.forms import MusicianForm
from .forms import AlbumForm


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'directory/album_form.html', {'form': form})

def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = AlbumForm()
    return render(request, 'directory/album_form.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('musician_list')

