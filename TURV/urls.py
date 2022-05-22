from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabels, name='tabels_url'),
    path('over/', views.over_tabels, name='over-tabels_url'),
    path('vac/', views.vac_tabels, name='vac-tabels_url'),
    path('nn/', views.nn_tabels, name='nn-tabels_url'),
    path('new/', views.new_tabel, name='new_tabel_url'),
    path('delcheck/<int:id>', views.tabel_delcheck, name='delcheck_url'),
    path('delete_checked/', views.del_tabel, name='del_tabel_url'),
    path('create/<int:id>', views.tabel_create, name='tabel_create_url'),
    path('additem/<int:id>', views.tabel_additem, name='tabel_addItem_url'),
    path('upditem/<int:id>', views.tabel_upditem, name='tabel_updItem_url'),
    path('delitem/<int:id>', views.tabel_delitem, name='tabel_delItem_url'),
    path('employers/', views.employers_list, name='emp_list'),
    path('employers/new', views.new_employer, name='emp_new'),
    path('employers/upd/<int:id>', views.upd_employer, name='emp_upd'),
    path('employers/del/<int:id>', views.del_employer, name='emp_del'),
    path('positions/', views.positions_list, name='pos_list'),
    path('positions/new', views.new_position, name='pos_new'),
    path('positions/upd/<int:id>', views.upd_position, name='pos_upd'),
    path('autos/', views.autos, name='autos_list'),
    path('autos/new', views.nr_autos, name='new_auto_url'),
    path('autos/edit/<int:id>', views.edit_autos, name='edit_auto_url'),
    path('messages/', views.messages_ref, name='messages_list'),
    path('messages/new/<int:id>', views.new_message, name='message_new_url'),
    path('unload/', views.unload, name='unload'),
    path('toxic-unload/', views.toxic_unload, name='toxic-unload'),
    path('unite-unload/', views.unite_unload, name='unite-unload'),
    path('checked/<int:id>', views.tabel_sup_check, name='checked'),
    path('comm/<int:id>/', views.upd_comm, name='comm'),
    path('overtime/', views.upd_norma, name='overtime_url'),
    path('overtime/upd', views.new_norma, name='overtime_new_url'),
    path('close/', views.w_close, name='close_url'),
    path('total/<str:month>/<str:year>/<int:dep>/', views.total_tabels, name='total_url'),
    path('total/open/', views.total_tabels_html, name='total_url_page')


     ]
