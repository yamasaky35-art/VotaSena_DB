from rest_framework.routers import DefaultRouter

from .views import (
    FichaViewSet,
    JornadaViewSet,
    ProgramaFormacionViewSet,
    ProgramaSedeViewSet,
    RolViewSet,
)

router = DefaultRouter()
router.register(r'programas-formacion', ProgramaFormacionViewSet, basename='programa-formacion')
router.register(r'programas-sede', ProgramaSedeViewSet, basename='programa-sede')
router.register(r'jornadas', JornadaViewSet, basename='jornada')
router.register(r'roles', RolViewSet, basename='rol')
router.register(r'fichas', FichaViewSet, basename='ficha')

urlpatterns = router.urls
