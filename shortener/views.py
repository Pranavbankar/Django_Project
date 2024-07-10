from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            return redirect('home')
    else:
        form = URLForm()
    
    urls = URL.objects.all()
    return render(request, 'shortener/home.html', {'form': form, 'urls': urls})


def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)


def delete_url(request, pk):
    url = get_object_or_404(URL, pk=pk)
    url.delete()
    return redirect('home')