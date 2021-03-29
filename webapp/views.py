from django.shortcuts import render
from django.views.generic import ListView
from .models import Webapp


# Create your views here.
class TableView(ListView):
    template_name = 'webapp.html'
    entries = Webapp.objects.all()
    display = {'entries': entries}
    
    def get(self, request):
        return render(request, self.template_name , self.display)
    