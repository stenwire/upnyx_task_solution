from django.contrib import admin


class UPNYXChatAdminSite(admin.AdminSite):
    site_header = "UPNYXChat Administration"
    site_title = "UPNYXChat"
    index_title = "UPNYXChat Administration"
    empty_value_display = "- - - -"


admin_site = UPNYXChatAdminSite(name="UPNYXChat Admin Site")
