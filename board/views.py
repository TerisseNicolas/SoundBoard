from django.shortcuts import render, redirect
from django.http import JsonResponse

from board.packages.soundfile import manager

from board.packages.forms.form import UploadFileForm


# Create your views here.

def index(request):
    names = manager.get_files_names()
    return render(request, 'index.html', {'names': names, 'upload_form': UploadFileForm()})


def play(request, name):
    manager.play(name)
    # todo no page reload
    return JsonResponse(status=200, data={"content": "todo play"})


def play_random(request):
    manager.play_random()
    # todo no page reload
    return JsonResponse(status=200, data={"content": "todo play"})


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            manager.upload(request.FILES['file'])
            return redirect('board.index')
        else:
            return redirect('board.error')
    else:
        return redirect('board.error')


def delete(request, name):
    manager.delete(name)
    return redirect('board.index')


def error(request):
    return render(request, 'error.html')
