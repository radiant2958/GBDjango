from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def home(request):
    logger.info('Посещение главной страницы')
    return render(request, 'mypages/index.html')

def about(request):
    logger.info('Посещение страницы обо мне ')
    return render(request, 'mypages/about.html')