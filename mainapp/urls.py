from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from .views import SearchConnectedView,SearchConnectedView_,ResultConnectedView_
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    )


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   # path('', views.home),
   path('v3/', SearchConnectedView.as_view()),
   path("v3/search/", SearchConnectedView_.as_view()),
   path("v3/result/<str:pk>/", ResultConnectedView_.as_view(), name="result"),

   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   # path("v3/search/", views.SearchConnectedView_),

]