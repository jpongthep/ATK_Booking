from django.contrib import admin
from .models import User_ATK, ATK_Lot, ATK_Queue

class User_ATK_FormAdmin(admin.ModelAdmin):
    list_display = ['PID']

class ATK_Queue_FormAdmin(admin.ModelAdmin):
    list_display = ['get_LotDate','get_LotNumber','Queue','user_atk','Statas','TimeStamp']
    ordering = ['-atk_lot__Lot_Date','atk_lot__Lot_Number','-Queue']
    list_filter = ['atk_lot__Lot_Time']
    date_hierarchy = 'atk_lot__Lot_Date'
    search_fields = ['user_atk__PID']
    list_editable = ['Statas']
    def get_LotDate(self, obj):
        return obj.atk_lot.Lot_Date
    get_LotDate.short_description = 'วันที่จอง'

    def get_LotNumber(self, obj):
        return obj.atk_lot.Lot_Time
    get_LotNumber.short_description = 'เวลา'
    

class ATK_Lot_FormAdmin(admin.ModelAdmin):
    list_display = ['Lot_Date','Lot_Number','Lot_Time','Lot_Total','Lot_Booking']
    ordering = ['Lot_Number']
    date_hierarchy = 'Lot_Date'

admin.site.register(User_ATK, User_ATK_FormAdmin)
admin.site.register(ATK_Queue, ATK_Queue_FormAdmin)
admin.site.register(ATK_Lot, ATK_Lot_FormAdmin)