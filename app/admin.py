from django.contrib import admin
from .models import Kulfi, Payment


class KulfiAdmin(admin.ModelAdmin):
    list_display = ["name", "amount", "payment_id", "paid"]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["payment_id", "order_id", "signature"]

admin.site.register(Kulfi, KulfiAdmin)
admin.site.register(Payment, PaymentAdmin)
