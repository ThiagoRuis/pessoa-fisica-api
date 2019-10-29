from pessoa_fisica.views import PessoaViewSet, EnderecoViewSet, TelefoneViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pessoa', PessoaViewSet, basename='pessoa')
router.register(r'endereco', EnderecoViewSet, basename='endereco')
router.register(r'telefone', TelefoneViewSet, basename='telefone')
urlpatterns = router.urls