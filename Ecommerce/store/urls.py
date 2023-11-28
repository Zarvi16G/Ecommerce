from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(store.urls)),
]
