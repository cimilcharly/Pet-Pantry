"""
URL configuration for Pantryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pantry import views

from django.conf import settings
from  django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('products', views.products),
    path('service', views.service),
    path('register', views.register),
    path('log', views.log),
    path('admin_h', views.admin_h),
    path('user_h', views.user_h),
    path('viewuser', views.viewuser),
    path('addproduct', views.addproduct),
    path('manageproduct', views.manageproduct),
    path('orderdetails', views.order),
    path('orderupdate', views.orderupdate),
    path('product', views.Product),

    path('cart', views.display_cart, name='cart'),
    path('add_cart/<int:d>',views.add_cart),
    path('delete_cart/<int:d>', views.deletecart),

    path('wishlist', views.wishlist, name='wishlist'),
    path('add_wishlist/<int:d>', views.add_wishlist),
    path('delete_wishlist/<int:d>', views.deletewishlist),
    path('delete_cart/<int:d>', views.deletecart),
    path('increment/<int:d>', views.increment),
    path('decrement/<int:d>', views.decrement),

    path('wishlist', views.wishlist),
    path('myorder', views.myorder),
    path('profile', views.profile),
    path('logout', views.logout),
    path('mform', views.mform),
    path('update_profile/', views.update_profile),
    path('delete/<int:d>',views.delete_product),
    path('update/<int:d>',views.update_product),

    path('payment/<int:l>/<int:d>/<int:k>', views.payment),
    path('payment_cart/<int:l>/<int:d>', views.paymentcart),
    path('payment_success', views.paymentsuccess),
    path('payment_success_cart', views.paymentsuccess_cart),

    path('checkout/<int:d>', views.checkout),
    path('checkout_cart/<int:total>/<int:qty>', views.checkoutcart),
    path('lowstock', views.lowstock),
    path('user_recent_orders', views.userrecentorders, name='user_recent_orders'),
    path('admin_recent_orders', views.adminrecentorders),
    path('admin_order_update/<int:d>', views.adminorderupdate),

    path('forgot', views.forgot_password),
    path('reset/<token>', views.reset_password),

    path('dbhome', views.dbhome),
    path('dblogin', views.dblogin),
    path('dbregister', views.dbregister),
    path('dbprofile', views.dbprofile),
    path('dborderdetails', views.dborderdetails),
    path('viewdb', views.viewdb),
    path('update_db/', views.update_db),
    path('Accept/<int:d>', views.Accept),
    path('Reject/<int:d>', views.Reject),
    path('reject_db/<int:d>', views.reject_db),
    path('accept_db/<int:d>', views.accept_db),
    path('delivered_update/<int:d>', views.delivered_update),

]
from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]