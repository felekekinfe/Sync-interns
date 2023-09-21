from django.shortcuts import render

# Create your views here.
import pyshorteners
from django import render

def shortner(request):
    short_url=''
    if request.method=='POST':
        long_url=request.POST.get('longurl')

        pyshort=pyshorteners.Shortener()
        try:
            short_url=pyshort.short(long_url)

            return render(request,'index.html',{'short_url':short_url})
        except:
            short_url=''

            return render(request,'index.html',{'short_url':short_url})
    else:
        return render(request,'index.html',{'short_url':short_url})

