from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.users import views
from apps.users.views import (
    ProfileCreateView, 
    ProfileListView, 
    ProfileRetrieveUpdateDestroyView
    )
from apps.dashboard.views import (
    ReportList, 
    ReportDetail, 
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    path('register/', views.RegistrationView.as_view()),
    path('auth/', views.AuthView.as_view()),

    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profiles/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),

    path('reports/', ReportList.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    path('report/export/', ReportExcelView.as_view(), name='report-export'),
    path('teams/',include('apps.dashboard.urls')),
]








