from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Expense
from django.contrib import messages
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='authentication/login')
def index(request):
    categories=Category.objects.all()
    expenses = Expense.objects.filter()
    
    context={
        'expenses': expenses
    }
    return render(request,'Expenses/index.html',context)

@login_required(login_url='authentication/login')
def Add_Expenses(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'Expenses/add_expenses.html', context)

    if request.method == 'POST':
        name=request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        date = request.POST['expense_date']
        amount = request.POST['amount']

        Expense.objects.create(name=name,description=description,category=category,date=date,amount=amount)
        messages.success(request, 'Expense saved successfully')

        return redirect('Expenses')

@login_required(login_url='authentication/login')
def Expense_Edit(request,id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()
    context = {
        'expense':expense,
        'values':expense,
        'categories':categories
    }
    if request.method=="GET":
        return render(request,'Expenses/edit_expenses.html',context)

    if request.method=="POST":
        name=request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        date = request.POST['expense_date']
        amount = request.POST['amount']

        expense.name=name
        expense.description=description
        expense.category=category
        expense.date=date
        expense.amount=amount
        expense.save()

        messages.success(request, 'Expense Updated successfully')

        return redirect('Expenses')

@login_required(login_url='authentication/login')       
def Expense_Delete(request,id):
    expense= Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request,'Expense Deleted')
    return redirect('Expenses')

def Search_Expense(request):
    if request.method =="POST":
        search_str = json.loads(request.body).get('searchText')
        expenses = Expense.objects.filter(
            name__istartswith=search_str) | Expense.objects.filter(
            description__istartswith=search_str) | Expense.objects.filter(
            category__icontains=search_str) | Expense.objects.filter(
            date__icontains=search_str)| Expense.objects.filter(
            amount__icontains=search_str)
        data = expenses.values()

        return JsonResponse(list(data),safe=False)
