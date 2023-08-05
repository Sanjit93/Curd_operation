from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
# this function add new function and show new function
def Add_show(request):
    if request.method == 'POST': 
        fm =StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            cm=fm.cleaned_data['mob_no']
            reg=User(name=nm,email=em, mob_no=cm)
            reg.save()
            fm =StudentRegistration()
    else:
        fm =StudentRegistration()
    stud=User.objects.all()
    return render(request, 'MyApp2/addandshow.html',{'form':fm,'stud':stud})
# this function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
# update data
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm =StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm =StudentRegistration(instance=pi)
    return render(request, 'MyApp2/updatestudent.html',{'form':fm})