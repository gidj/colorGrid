from django.shortcuts import render
from utils import random_octal_str

def index(request):
    """ Just render the form asking for the number of cells to generate """
    return render(request, 'index.html')

def grid(request):
    """ If a number is submitted via the form at index, use it; otherwise,
    use 3 """

    if 'number' in request.GET and request.GET['number']:
        n = int(request.GET['number'])
    else:
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

