from django.db import models
from datetime import date


# -----------------------------------------------------------------------------------------------------------------------------

class User_ATK (models.Model) :
    class Meta:
        verbose_name_plural = "ผู้ลงทะเบียน"

    PID = models.CharField(max_length = 13, blank = True, null = True, verbose_name = 'เลขบัตรประชาชน')

    def __str__(self):
        return f'{self.PID}'

    

# -----------------------------------------------------------------------------------------------------------------------------

class ATK_Lot (models.Model) :
    class Meta:
        verbose_name_plural = "ตารางเวลาการตรวจ"  
      
    Lot_Number = models.IntegerField(blank=True, null=True,verbose_name="ล็อตที่")
    Lot_Time = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="เวลาที่นัดจอง")
    Lot_Total = models.IntegerField(
        null=True, blank=True, default='', verbose_name="จำนวนการเปิดจอง")
    Lot_Date = models.DateField(null=True,blank=True, verbose_name="วันที่ต้องการจอง")
    

    Lot_Booking = models.IntegerField(
        verbose_name="จำนวนที่จองไปแล้ว")
   
    def __str__(self):
        return f'{self.Lot_Date},{self.Lot_Time}'

# -----------------------------------------------------------------------------------------------------------------------------

class ATK_Queue (models.Model) :
    class Meta:
        verbose_name_plural = "การจัดการคิว"
        ordering = ["id"]

    user_atk = models.ForeignKey(
        User_ATK,
        null=True,
        blank=True,
        on_delete = models.DO_NOTHING,
        related_name='User_ATK_FK') 

    atk_lot = models.ForeignKey(
        ATK_Lot,
        null=True,
        blank=True,
        on_delete = models.DO_NOTHING,
        related_name='ATK_Lot_FK',
        verbose_name="ล็อตที่")
  
    StatusChoice = [('101', 'ยังไม่ได้รับการตรวจ'),
                        ('102', 'ตรวจแล้ว'),]

    Statas = models.CharField(
        max_length=20,
        choices=StatusChoice,
        default='102',
        verbose_name="สถานะเข้ารับบัตรคิว")    
    Queue = models.IntegerField(null=True, blank=True, verbose_name="คิวที่")
    TimeStamp = models.DateTimeField(auto_now_add=True, null=True, verbose_name = "เวลาที่บันทึก")

    def __str__(self):
        return f'{self.user_atk} : {self.Statas} : {self.Queue} : {self.TimeStamp}'