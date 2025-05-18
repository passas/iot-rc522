from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Contract, Ticket, Train, TemperatureHumidity

class _UserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role','card_id',)}),
    )
admin.site.register(User, _UserAdmin)

class ContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = ['get_username', 'get_first', 'get_last', 'type', 'zone1', 'zone2', 'price']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'type', 'zone1', 'zone2', 'price']
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Email'
    get_username.admin_order_field = 'user__username'
    def get_first(self, obj):
        return obj.user.first_name
    get_first.short_description = 'First'
    get_first.admin_order_field = 'user__first_name'
    def get_last(self, obj):
        return obj.user.last_name
    get_last.short_description = 'Last'
    get_last.admin_order_field = 'user__last_name'
admin.site.register(Contract, ContractAdmin)

class TicketAdmin(admin.ModelAdmin):
    model = Ticket
    list_display = ['card_id', 'type', 'zone1', 'zone2', 'amount']
    search_fields = ['card_id', 'type', 'zone1', 'zone2', 'amount']
admin.site.register(Ticket, TicketAdmin)

class TrainAdmin(admin.ModelAdmin):
    model = Train
    list_display = ['id']
    search_fields = ['id']
admin.site.register(Train, TrainAdmin)

class TemperatureHumidityAdmin(admin.ModelAdmin):
    model = TemperatureHumidity
    list_display = ['id', 'train_id', 'temperature', 'humidity', 'timestamp']
    search_fields = ['id', 'train_id', 'temperature', 'humidity', 'timestamp']
admin.site.register(TemperatureHumidity, TemperatureHumidityAdmin)
