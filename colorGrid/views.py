from django.shortcuts import render
from utils import random_octal_str

def index(request):
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

