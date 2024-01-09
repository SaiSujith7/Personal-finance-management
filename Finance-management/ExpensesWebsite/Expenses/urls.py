from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="Expenses"),
    path('Add_Expenses',views.Add_Expenses,name="Add_Expenses"),
    path('Expense_Edit/<int:id>',views.Expense_Edit,name="Expense_Edit"),
    path('Expense_Delete/<int:id>',views.Expense_Delete,name="Expense_Delete"),
    path('Search_Expense',views.Search_Expense,name="Search_Expense"),

]