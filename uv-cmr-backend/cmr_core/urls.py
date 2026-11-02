from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='inicio'),
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='api_token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
    
    # documentación swagger 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
]