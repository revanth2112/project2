from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from napp.models import Employee
from napp.forms import EmployeeForm
from napp.forms import SignUpForm

# Create your views here.

def home(request):
	return render(request,'napp/home.html')

@login_required
def hr(request):
	return render(request,'napp/hr.html')

def emp(request):
	return render(request,'napp/employee.html')

@login_required
def emp_form(request):
	form=EmployeeForm()
	if request.method=="POST":
		form=EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/empdata')
	return render(request,'n/empform.html',{'form':form})

@login_required
def emp_data(request):
	employees=Employee.objects.all()
	return render(request,'napp/empdata.html',{'employees':employees})

@login_required
def delete(request,id):
	employee=Employee.objects.get(id=id)
	employee.delete()
	return redirect('/empdata')

@login_required
def update(request,id):
	employee=Employee.objects.get(id=id)
	if request.method=="POST":
		form=EmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
		return redirect('/empdata')
	return render(request,'napp/update.html',{'employee':employee})

def news(request):
	return render(request,'napp/addnews.html')

def logout(request):
	return render(request,'napp/logout.html')

def signup(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'napp/signup.html',{'form':form})