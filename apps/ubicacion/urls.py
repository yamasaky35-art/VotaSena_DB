from rest_framework.routers import DefaultRouter

from .views import DepartamentoViewSet, MunicipioViewSet

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'municipios', MunicipioViewSet, basename='municipio')

urlpatterns = router.urls
