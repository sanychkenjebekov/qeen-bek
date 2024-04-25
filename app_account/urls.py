from django.urls import path,include
from app_account.views import (UserInfoApiView, LogoutView, PaymentMethodApiView,
SendResetAPiView, ChangePasswordAPIVIew, ChangeUserInfoApiView, 
HistoryCreateApiView, HistoryListApiView, UserUpdateApiView, HistoryDetailView, HistoryByUserListApiView
)


urlpatterns = [
    path('user/info/', UserInfoApiView.as_view()),
    path('user/update/', UserUpdateApiView.as_view()),
    path('logout/user/', LogoutView.as_view(), name='user logout'),
    path('payment/method/', PaymentMethodApiView.as_view()),
    path('change/user/', ChangeUserInfoApiView.as_view()),
    path('history/list/', HistoryListApiView.as_view()),
    path('history/by/user/', HistoryByUserListApiView.as_view()),
    path('history/change/<int:id>/', HistoryDetailView.as_view()),
    path('history/create/', HistoryCreateApiView.as_view()),
    path('send/reset/code/', SendResetAPiView.as_view()),
    path('change/password/', ChangePasswordAPIVIew.as_view()),


]