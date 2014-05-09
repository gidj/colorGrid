from django.shortcuts import render
from utils import random_octal_str

def default(request):
    grid = []
    for row in xrange(3):
        r = []
        for cell in xrange(3):
            r.append(random_octal_str(9))
        grid.append(r)

    context = {'grid': grid,
               'title': 'Grid',}
    return render(request, 'index.html', context)

