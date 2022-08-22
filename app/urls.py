from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view(), name="home"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('detail/<id>/', ProductDetailView.as_view(), name="detail"),
    path('history/', OrderHistoryListView.as_view(), name="history"),
    path('failed/', PaymentFailedView.as_view(), name="failed"),
    path('success/', PaymentSuccessView.as_view(), name="success"),
    path('api/checkout-session/<id>/',
         create_checkout_session, name='api_checkout_session'),
]
