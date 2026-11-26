from rest_framework.routers import DefaultRouter

from .views import (
    ActaViewSet,
    ComiteElectoraViewSet,
    EleccionViewSet,
    ListaViewSet,
    VotoViewSet,
)

router = DefaultRouter()
router.register(r'elecciones', EleccionViewSet, basename='eleccion')
router.register(r'actas', ActaViewSet, basename='acta')
router.register(r'comites', ComiteElectoraViewSet, basename='comite-electora')
router.register(r'votos', VotoViewSet, basename='voto')
router.register(r'listas', ListaViewSet, basename='lista')

urlpatterns = router.urls
