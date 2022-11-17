from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include,re_path
from rest_framework import routers
from rest_framework import permissions
from API_Opens.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from API_Opens import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'abogado',AbogadoViewSet)
router.register(r'plantilla',PlantillaViewSet)
router.register(r'solicitud',SolicitudViewSet)
router.register(r'documento',DocumentoViewSet)
router.register(r'cliente',ClienteViewSet)
router.register(r'user',UserViewSet)
router.register(r'group',GroupViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="API Opens",
      default_version='v1',
      description="Documentacion API Opens",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'documentacion/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #! LOGEO
    path('',views.signin, name='signin'), 
    path('signup/',views.signup, name='signup'),
    path('signup2/',views.signup2, name='signup2'),
    path('signout/',views.signout, name='signout'),
    #!ABOGADO
    path('ahome/',views.ahome, name='ahome'),
   #  path('agregarcli/<str:username>/',views.agregarcli, name='agregarcli'),
   #  path('modificarcli/<str:username>/',views.modificarcli, name='modificarcli'),
   #  path('eliminarcli/<str:username>/',views.eliminarcli, name='eliminarcli'),
    #!PERFIL
    path('miperfil/<str:username>/',views.miperfil, name='miperfil'),
    path('perfilcli/<str:username>/',views.perfilcli, name='perfilcli'),
    path('modificarperfilc/',views.modificarcliente, name='modificarcliente'),
    path('modificarperfila/',views.modificarabogado, name='modificarabogado'),
    #!CLIENTE
    path('hola/',views.hola, name='hola'),
   #!Documentos
    path('cargarDoc/',views.uploadFile, name='cargarDoc'),
    path('eliminardoc/',views.eliminardoc, name='eliminardoc'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

