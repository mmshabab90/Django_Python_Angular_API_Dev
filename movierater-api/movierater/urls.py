
from django.conf.urls import url, include
from django.contrib import admin

# Access the url file located in api folder
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('movierater.api.urls'))
]
