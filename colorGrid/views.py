from django.shortcuts import render
def default(request):
    grid = []
    for row in xrange(1, 10, 3):
        grid.append(range(1*row, (row+3)))

    context = {'grid': grid,
               'title': 'Grid',}
    return render(request, 'index.html', context)

