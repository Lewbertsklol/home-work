from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def feedback(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'catalog/feedback.html')
