from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import MedForm,SearchForm
from .models import Medicine
from django.db.models import Q




@login_required(login_url='loginpage')
def userpage(request):
    return render(request,'home.html')

def add_med(request):
    if request.method=='POST':
        form=MedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form=MedForm()
    return render(request,'add.html',{'form':form})

def list_med(request):
    # med_list=Medicine.objects.all()
    below_50=Medicine.objects.filter(price__lt=50)
    btw_50_100=Medicine.objects.filter(Q(price__gte=50) & Q(price__lte=100))
    above_100=Medicine.objects.filter(price__gt=100)
    context={'below_50':below_50,'btw_50_100':btw_50_100,'above_100':above_100}
    return render(request,'edit.html',context)

def update_med(request,id):
    med=Medicine.objects.get(id=id)
    if request.method=='POST':
        form=MedForm(request.POST,instance=med)
        if form.is_valid():
            form.save()
            return redirect('listmed')
    else:
        form=MedForm(instance=med)
    return render(request,'update.html',{'form':form})

def del_med(request,id):
    med=Medicine.objects.get(id=id)
    if request.method=='POST':
        med.delete()
        return redirect('listmed')
    return render(request,'delete.html',{'med':med})

def search_med(request):
    form=SearchForm(request.GET)
    results=[]
    if form.is_valid():
        query=form.cleaned_data['query']
        results=Medicine.objects.filter(Q(name__istartswith=query) | Q(price__icontains=query))
        
    return render(request,'results.html',{'form':form,'results':results})


# below 50--one color
# b/w 50 and 60--one color
# above 100--one color for price