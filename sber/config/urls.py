from django.conf import settings
from django.contrib import admin
from django.urls import path

from deposit.views import DepositCalculationView
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'calculation_deposit/',
        DepositCalculationView.as_view(),
        name='calculation_deposit'
    ),
]

urlpatterns += doc_urls
