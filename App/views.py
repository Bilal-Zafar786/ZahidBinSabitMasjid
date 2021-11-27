from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import StudentRegister
# Create your views here.
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
def show(request):
    student = StudentRegister.objects.all()
    return render(request,"show.html",{'student':student})
def edit(request, id):
    student = StudentRegister.objects.get(Roll_Number=id)
    return render(request,'edit.html', {'student':student})
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
def destroy(request, id):
    employee = StudentRegister.objects.get(Roll_Number=id)
    employee.delete()
    return redirect("/show")