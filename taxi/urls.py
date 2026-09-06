from django.urls import path

from taxi.views import index

urlpatterns = [

    path("", index, name="index")
    # path("", site.urls),
]

app_name = "taxi"
