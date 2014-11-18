#-*- enconding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^crud-pessoa/', 'crud_pessoa.views.cadastro_pessoa', name='cadastro.pessoa'),
)
