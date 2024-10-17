from django.urls import path
from . import views
urlpatterns = [
    path('buses/', views.buses, name='buses'),
    path('', views.home, name='home'),
    path('registor/', views.registor, name='registor'),
    path('profile/', views.profile, name='profile'),
    path('buses/', views.buses, name='buses'),
    path('offers/', views.offers, name='offers'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/login', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('root/', views.root, name='root'),
    path('users/', views.users, name='users'),
    path('comments/', views.comments, name='comments'),
    path('routes/', views.routes, name='routes'),
    path('Selectbus/', views.Selectbus, name='Selectbus'),
    path('ticket/', views.ticket, name='ticket'),
    path('businsert/', views.businsert, name='businsert'),
    path('comment/', views.comment, name='comment'),
    path('worker/', views.worker_view, name='worker'),
    path('Showtickets/', views.Showtickets, name='Showtickets'),
    path('delete_ticket/', views.delete_ticket, name='delete_ticket'),
    path('delete_tickets/', views.delete_tickets, name='delete_tickets'),
    path('delete_ticketss/', views.delete_ticketss, name='delete_ticketss'),
    path('route/', views.route, name='route'),
    path('driver/', views.driver, name='driver'),
    path('city/', views.city_view, name='city'),
    path('city/city', views.city_view, name='city_view'),
    path('ticketinfo/', views.ticketinfo, name='ticketinfo'),
    path('ticketinfo/ticketinfo', views.ticketinfo, name='ticketinfo'),
    path('worker/worker', views.worker_view, name='worker'),
    #path('changebus/changebus', views.changebus, name='changebus'),
    path('route/route', views.route, name='route'),
    path('routedelete/', views.routedelete, name='routedelete'),
    path('admins/', views.admins, name='admins'),
    path('ad/', views.ad, name='ad'),
    path('get_user/', views.get_user, name='get_user'),
    path('get_route/', views.get_route, name='get_route'), 
    path('ticketinfo/', views.ticketinfo, name='ticketinfo'),
    path('get_ticket/',views.get_ticket, name='get_ticket'),
    #path('get_ticket/get_ticket',views.get_ticket, name='get_ticket'),
    path('selectbus/', views.selectbus, name='selectbus'),
    path('book/', views.book, name='book'),
    path('Select/', views.Select, name='Select'),
    path('details/', views.details, name='details'),
    path('admindelete/', views.admindelete, name='admindelete'),
    path('delete/', views.delete, name='delete'),
    path('routedelete/', views.routedelete, name='routedelete'),
    path('workerdelete/', views.workerdelete, name='workerdelete'),
    path('busdelete/', views.busdelete, name='busdelete'),
    path('delete_tickets/', views.delete_tickets, name='delete_tickets'),
    path('citydelete/', views.citydelete, name='citydelete'),
    path('commentdelete/', views.commentdelete, name='commentdelete'),
    path('updatebus/', views.updatebus, name='updatebus'),
    path('changebus/', views.changebus, name='changebus'),
    path('changebuses/', views.changebuses, name='changebuses'),
    path('changebus/changebus/', views.changebus, name='changebus')

]
