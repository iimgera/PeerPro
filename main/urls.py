from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.users import views
from apps.users.views import (
    UserCreateView, 
    UserListView, 
    UserRetrieveUpdateDestroyView
    )






schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


api_v1 = [
    path('register/', views.RegistrationView.as_view()),
    path('auth/', views.LoginView.as_view()),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),

]
from django.urls import path, include 

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.dashboard.views import (
    ReportList, ReportDetail, 
    ReportExcelView, 
    )


schema_view = get_schema_view(
    openapi.Info(
        title="PeerPro API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('reports/', ReportList.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    path('report/export/', ReportExcelView.as_view(), name='report-export'),
    path('teams/',include('apps.dashboard.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]








