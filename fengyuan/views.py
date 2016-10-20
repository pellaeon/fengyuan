from django.shortcuts import redirect


def index(request):
    return redirect('files:index', permanent=True)
