from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import StudentRegister

from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def emp(request):
    if request.method == "POST":
        print("ifff")
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                print("Saving")
                return redirect('/show')
            except:
                print("Not Saving")
        else:
            print("Not Valid")
    else:
        form = RegistrationForm()
        # print(form.as_p())
        print("Else")
    return render(request,'index.html',{'form':form})
@login_required
def show(request):
    student = StudentRegister.objects.all()
    return render(request,"show.html",{'student':student})
@login_required
def edit(request, id):
    student = StudentRegister.objects.get(Roll_Number=id)
    return render(request,'edit.html', {'student':student})
@login_required
def update(request, id):
    student = StudentRegister.objects.get(Roll_Number=id)
    print(student.Address)
    form = RegistrationForm(request.POST, instance=student)
    print("Updating")
    if form.is_valid():
        form.save()
        print("Updated")
        return redirect("/show")
    else:
        print("Not Valid")
    return render(request, 'edit.html', {'student': student})
@login_required
def destroy(request, id):
    employee = StudentRegister.objects.get(Roll_Number=id)
    employee.delete()
    return redirect("/show")


def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=pwd)
            login(request, user)
            return redirect('emp')
    form=SignupForm
    return render(request, 'registration/signup.html',{'form':form})
