from django.shortcuts import render



import logging
logger = logging.getLogger('HousingLog.views')

def home(request):
    
    logger.info('open home page')
    return render(request,'_base.html')
# Create your views here.
