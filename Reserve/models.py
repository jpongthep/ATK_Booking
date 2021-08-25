from django.db import models
import datetime

def tomorrow():
    _tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return _tomorrow

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
        constraints = [
            models.UniqueConstraint(fields=['Lot_Date', 'Lot_Number'], name='Date_Slot')
        ]
    Lot_Date = models.DateField(verbose_name="วันที่ต้องการจอง", null=True,blank=True, default=tomorrow )  
    Lot_Number = models.IntegerField(blank=True, null=True,verbose_name="ล็อตที่")
    TimeChoice = [('08:00 - 09:00', '08:00 - 09:00'),
                ('09:00 - 10:00', '09:00 - 10:00'),
                ('10:00 - 11:00', '10:00 - 11:00'),
                ('11:00 - 12:00', '11:00 - 12:00'),
                ('13:00 - 14:00', '13:00 - 14:00'),]
    Lot_Time = models.CharField(choices = TimeChoice,
        max_length=15, null=True, blank=True, verbose_name="เวลาที่นัดจอง")
    Lot_Total = models.IntegerField(
        null=True, blank=True, default=200, verbose_name="จำนวนการเปิดจอง")   
    
    Lot_Booking = models.IntegerField(
        verbose_name="จำนวนที่จองไปแล้ว", default=0)
   
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