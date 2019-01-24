from django.urls import path

from . import views

urlpatterns = [
    path('', views.principal, name = 'cliente'),
    path('primerMensaje', views.saludar),
    path('nuevo', views.crear),
    path('editar', views.modificar),
    path('eliminar', views.eliminar),
    path('activar',views.activar),
    path('buscar',views.buscar),
    path('buscarCuenta',views.buscarCuenta),
    path('buscarC',views.buscarC),
    path('listar',views.listartodos),
    path('cuentas', views.principalCuenta),
    path('crearCuenta', views.crearCuenta),
    path('eliminarC',views.eliminarCuenta),
    path('activarC',views.activarCuenta),
    path('listarC',views.listarCuenta),
    path('transaccion', views.transaccion),
    path('verTransaccion', views.verTransaccion),
    path('transferencia', views.crearTransferencia),
    path('buscarCuentaTransferencia', views.buscarTrans),

]
