#
# Copyright (C) 2024 Arpa Piemonte - Dipartimento Naturali e Ambientali
# This file is part of weboll (the bulletin back-office for ARPA Piemonte).
# weboll is licensed under the AGPL-3.0-or-later License.
# License text available at https://www.gnu.org/licenses/agpl.txt
#
#
from django.urls import include, path
from rest_framework import routers

from w12.back import views

router = routers.DefaultRouter()
router.register(r"bulletins", views.W12View)
router.register(r"data", views.W12DataView)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
    path(
        "svg/<int:pk>",
        views.W12SVGView.as_view(),
        name="w12-svg",
    ),
    path("pdf/<int:pk>", views.W12PDFView.as_view(), name="w12-pdf"),
    path(
        "arpapiemonte/<int:pk>",
        views.ArpaPiemonteView.as_view(content_type="text/xml"),
        name="a7-a26-arpapiemonte",
    ),
]
