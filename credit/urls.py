from django.contrib import admin
from django.urls import path
from account.views import Import
from account.views import register, check_eligibility, create_loan, ViewLoan, ViewLoans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import', Import.as_view()), #importing test data into database
    path('register', register.as_view()),
    path('check-eligibility', check_eligibility.as_view(), name='check-eligibility'),
    path('create-loan', create_loan.as_view()),
    path('view-loan/<int:id>', ViewLoan.as_view()),
    path('view-loans/<int:id>', ViewLoans.as_view()),
]
