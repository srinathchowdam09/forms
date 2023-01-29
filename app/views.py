from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form(request):
    if request.method=='POST':
        un=request.POST['srinath']
        pw=request.POST['1432']
        print('un')
        print('pw')
        return HttpResponse('data is submiited')
        

    return render(request,'form.html')
