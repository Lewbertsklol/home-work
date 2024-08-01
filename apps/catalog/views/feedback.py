from django.views import generic
from django.shortcuts import redirect, render
# Create your views here.


class FeedbackView(generic.View):

    def get(self, request):
        return render(request, 'catalog/feedback.html')

    def post(self, request):
        return redirect('catalog:product_list')
