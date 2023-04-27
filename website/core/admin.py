#
# Copyright (C) 2020-2023 simevo s.r.l. for ARPA Piemonte - Dipartimento Naturali e Ambientali
# This file is part of weboll (the bulletin back-office for ARPA Piemonte).
# weboll is licensed under the AGPL-3.0-or-later License.
# License text available at https://www.gnu.org/licenses/agpl.txt
#
#
from django.contrib import admin
from django.contrib.admin.models import DELETION
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

from w22.back.models import W22
from w22verifica.back.models import W22Verifica
from w23.back.models import W23, W23Data
from w24.back.models import W24, W24Data
from w29.back.models import W29
from w30.back.models import W30, W30Data
from w31.back.models import W31
from w32.back.models import W32

from .models import W05, W16, Bulletins, Destinazioni, W05Data, W16Data

admin.register(
    W05,
    W05Data,
    W16,
    W16Data,
    W22,
    W22Verifica,
    W23,
    W23Data,
    W24,
    W24Data,
    W29,
    W30,
    W30Data,
    W31,
    W32,
)(admin.ModelAdmin)


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = "action_time"

    # to filter the resultes by users, content types and action flags
    list_filter = ["user", "content_type", "action_flag"]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "action_flag",
        "change_message",
        "object_link",
    ]

    list_select_related = True

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        text = escape(obj.object_repr)
        if obj.action_flag == DELETION:
            link = text.strip()
        else:
            ct = obj.content_type
            url = reverse(
                "admin:%s_%s_change" % (ct.app_label, ct.model),
                args=(obj.object_id,),
            )
            link = '<a href="%s">%s</a>' % (url.strip(), text.strip())
        return mark_safe(link)


@admin.register(Destinazioni)
class DestinazioniAdmin(admin.ModelAdmin):

    list_display = ["prodotto", "destinazione", "endpoint", "segreto", "enabled"]


@admin.register(Bulletins)
class BulletinsAdmin(admin.ModelAdmin):

    list_display = ["prodotto", "auto", "time"]
