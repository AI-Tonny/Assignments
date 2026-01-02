from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet
from news.views import NewsViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/auth/', include('auth.urls'))
]
