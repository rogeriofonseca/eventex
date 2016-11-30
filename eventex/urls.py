from django.conf.urls import include, url
from django.contrib import admin
# importe explicitamente o modulo da view e passe a funcao view como 
# parametro para a funcao url()
from eventex.core.views import home
from eventex.subscriptions.views import detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/', include('eventex.subscriptions.urls', 
                                namespace='subscriptions')),
    url(r'^admin/', admin.site.urls),
]
