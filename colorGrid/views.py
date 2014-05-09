from django.shortcuts import render
from django.http import HttpResponseRedirect
from utils import random_octal_str
import colorGrid.models.GridForm

def index(request):
    if request.method == "POST":
        form = GridForm(request.POST)
        if form.is_valid():
            pass

    return render(request, 'index.html')

def grid(request):
    n = 3;

    grid = []
    for row in xrange(n):
        r = []
        for cell in xrange(n):
            r.append(random_octal_str(9))
        grid.append(r)

    context = {'grid': grid,
               'title': 'Grid',}
    return render(request, 'grid.html', context)

