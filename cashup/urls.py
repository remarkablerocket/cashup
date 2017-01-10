from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SimpleHomeRedirectView.as_view(),
        name='home'),
    url(r'^business/$', views.BusinessUpdateView.as_view(),
        name='cashup_business_update'),
    url(r'^outlets/$', views.OutletListView.as_view(),
        name='cashup_outlet_list'),
    url(r'^outlets/(?P<name>[\w.@+-]+)/$',
        views.OutletClosureListView.as_view(),
        name='cashup_outlet_detail'),
    url(r'^outlets/(?P<name>[\w.@+-]+)/settings/$',
        views.OutletUpdateView.as_view(),
        name='cashup_outlet_settings'),
    url(r'^outlet/new/$',
        views.OutletCreateView.as_view(),
        name='cashup_outlet_create'),
    url(r'^closures/(?P<pk>[0-9]+)/$',
        views.TillClosureDetailView.as_view(),
        name='cashup_closure_detail'),
    url(r'^closures/(?P<pk>[0-9]+)/edit/$',
        views.TillClosureUpdateView.as_view(),
        name='cashup_closure_update'),
    url(r'^outlets/(?P<name>[\w.@+-]+)/close-till/$',
        views.TillClosureCreateView.as_view(),
        name='cashup_closure_create'),
]
