from django.contrib import admin
from .models import User_ATK, ATK_Lot, ATK_Queue

class User_ATK_FormAdmin(admin.ModelAdmin):
    list_display = ['PID']

class ATK_Queue_FormAdmin(admin.ModelAdmin):
    list_display = ['user_atk','Statas','atk_lot','Queue','TimeStamp']
    
class ATK_Lot_FormAdmin(admin.ModelAdmin):
    list_display = ['Lot_Number','Lot_Time','Lot_Total','Lot_Date','Lot_Booking']

admin.site.register(User_ATK, User_ATK_FormAdmin)
admin.site.register(ATK_Queue, ATK_Queue_FormAdmin)
admin.site.register(ATK_Lot, ATK_Lot_FormAdmin)