from rest_framework.routers import DefaultRouter

from .views import (
    BienestarAprendizViewSet,
    CentroFormacionViewSet,
    SedeViewSet,
)

router = DefaultRouter()
router.register(r'centros-formacion', CentroFormacionViewSet, basename='centro-formacion')
router.register(r'bienestar', BienestarAprendizViewSet, basename='bienestar-aprendiz')
router.register(r'sedes', SedeViewSet, basename='sede')

urlpatterns = router.urls
