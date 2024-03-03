from django.contrib import admin
from django.urls import path

from deposit.views import DepositCalculationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'calculation_deposit/',
        DepositCalculationView.as_view(),
        name='calculation_deposit'
    ),
]
