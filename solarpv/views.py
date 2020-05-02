from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from backend.models import Certificate
from django.contrib import messages
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from  .serializers import CertificateSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

#provides default model view due to inheriting ModelViewSet
#class CertificateViewSet(viewsets.ModelViewSet): 
   # queryset = Certificate.objects.all()
   # serializer_class = CertificateSerializer

#provides custom view due to inheriting ViewSet
class CertificateViewSet(viewsets.ViewSet): 
    def list(self, request):
        queryset = Certificate.objects.all()
        serializer  = CertificateSerializer(queryset, many=True)
        return Response(serializer.data)


def certificationSearch(request):
    queryset = Certificate.objects.all()
    context = {
        "object_list": queryset,
    }

    if request.method ==  'POST':
        searchTxt = request.POST['searchInput']

        if searchTxt:
            matchQset = Certificate.objects.filter(Q(certificate_number__icontains=searchTxt) | 
                                                    Q(id__icontains=searchTxt) | 
                                                    Q(report_number__icontains=searchTxt))

            if matchQset:
                return render(request, 'certification-search.html', {"object_list": matchQset, "sTxtAfter" : searchTxt})
            else:                
                messages.error(request, 'No matching result found.')
                return render(request, 'certification-search.html',{})
        else:
            return HttpResponseRedirect('certification-search')
    
    else:
        return render(request, 'certification-search.html',context)
    