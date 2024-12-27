from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework . permissions import AllowAny

schmea_view = get_schema_view(
    openapi.Info(
        title="API DOC",
        default_version="v1",
        description="Doc de l'API",
    ),
    public=True,
    permission_classes=(AllowAny,),

)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api_app.urls")),

    # doc urls
    path('swagger/', schmea_view.with_ui('swagger',cache_timeout =0), name='swagger'),
    path('redoc/', schmea_view.with_ui('redoc',cache_timeout =0), name='redoc'),

]
