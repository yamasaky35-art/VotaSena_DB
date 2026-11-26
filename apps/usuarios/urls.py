from rest_framework.routers import DefaultRouter

from .views import AprendizViewSet, CandidatoPostuladoViewSet, PersonaViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='persona')
router.register(r'aprendices', AprendizViewSet, basename='aprendiz')
router.register(r'candidatos', CandidatoPostuladoViewSet, basename='candidato-postulado')

urlpatterns = router.urls
