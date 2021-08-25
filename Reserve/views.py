from django.shortcuts import render , redirect , get_object_or_404

from django.contrib import messages
from Reserve.models import User_ATK, ATK_Lot, ATK_Queue

from datetime import timedelta
from django.utils import timezone
import datetime

def tomorrow():
    _tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    return _tomorrow

def Booking (request):
    hour = timezone.now().hour+7    
    if not 8 <= hour <= 15 : 
        return render(request, 'reserve_p/reserve_close.html')    
    show_lot = ATK_Lot.objects.filter(Lot_Date = tomorrow()).all()
    index = {'show_lot': show_lot}    
    if request.method == 'POST':
        if request.POST.get('pid1') and request.POST.get('select_lot'): 
            PIDList = []
            if request.POST.get('pid1'):
                PIDList.append(request.POST.get('pid1'))
            if request.POST.get('pid2'):
                PIDList.append(request.POST.get('pid2'))
            if request.POST.get('pid3'):
                PIDList.append(request.POST.get('pid3')) 
            for CountPID in PIDList:
                User = User_ATK.objects.filter(PID = CountPID)                
                if User.exists():
                    last14days = timezone.now().date() - timedelta(days=14)
                    if ATK_Queue.objects.filter(user_atk = User[0]).filter(TimeStamp__gte = last14days).filter(Statas = "102").exists() :
                        messages.error(request, 'รอ 14 วัน')
                    else :
                        messages.success(request, "Next")
                        queue = ATK_Queue()  
                        Booking = ATK_Lot.objects.get(id = request.POST.get('select_lot'))
                        Booking.Lot_Booking += 1
                        Booking.save()

                        getLotID = ATK_Lot(id = request.POST.get('select_lot'))                    
                        queue.atk_lot = getLotID 
                        queue.user_atk = User[0] 

                        MyQueue = Booking.Lot_Booking                    
                        queue.Queue = MyQueue
                        queue.save()
                else :
                    User = User_ATK (PID =CountPID)
                    User.save()
                    queue = ATK_Queue()  
                    Booking = ATK_Lot.objects.get(id = request.POST.get('select_lot'))
                    Booking.Lot_Booking += 1
                    Booking.save()

                    getLotID = ATK_Lot(id = request.POST.get('select_lot')) 
                    queue.atk_lot = getLotID 
                    queue.user_atk = User 

                    MyQueue = Booking.Lot_Booking                    
                    queue.Queue = MyQueue
                    queue.save()

            get_lot_detail = ATK_Lot.objects.filter(id = request.POST.get('select_lot'))
            get_queue_detail = ATK_Queue.objects.filter(atk_lot_id = request.POST.get('select_lot')).filter(user_atk__PID__in = PIDList)
            print(get_queue_detail)

            context = {'get_queue_detail': get_queue_detail}  


            return render (request, "reserve_p/reserve_detail.html" , context)

    return render(request, "reserve_p/reserve_create.html", index)


def Search_Page (request):
    context = {}
    print(request.method)
    if request.method == 'POST' :
        search = request.POST.get('search')
        print(request.POST)
        User = User_ATK.objects.filter(PID = search)
        if User.exists():
            queue = ATK_Queue.objects.filter(user_atk = User[0])    
            print(queue)
        else:
            return render (request, "reserve_p/reserve_nodata.html")

        context = {'user': User , 'queue': queue}

        return render (request, "reserve_p/reserve_detail.html" , context)

    return render(request, 'reserve_p/reserve_search.html', context)


