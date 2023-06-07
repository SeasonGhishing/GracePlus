from django.urls import include, path
from .views import MemberGetCreate, MemberGetUpdateDelete

urlpatterns = [
    path('', MemberGetCreate.as_view()),
    path('<int:pk>', MemberGetUpdateDelete.as_view)
]
