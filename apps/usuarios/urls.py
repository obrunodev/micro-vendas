from django.urls import include, path

app_name = 'usuarios'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
