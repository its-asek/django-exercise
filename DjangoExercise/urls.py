from django.urls import path, include


urlpatterns = [
    path("", include("apps.home_page.urls")),
    path("text-processor/", include("apps.text_processor.urls")),
    path("pesel-decoder/", include("apps.pesel_decoder.urls")),
]
