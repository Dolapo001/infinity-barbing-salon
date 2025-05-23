from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<str:ticket_number>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('stylist-appointments/', StylistAppointmentListView.as_view(), name='stylist-appointments'),
    path('appointments-by-day/', AppointmentListByDayView.as_view(), name='appointments')
]
