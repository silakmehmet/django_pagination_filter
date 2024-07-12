from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PathMVS, StudentMVS

router = DefaultRouter()
router.register("paths", PathMVS)
router.register("students", StudentMVS)


urlpatterns = [
    path("", include(router.urls))
]
