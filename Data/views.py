from django.shortcuts import render
from django.http import HttpResponse
from .task import collect_daily_data


def home(request):

    return HttpResponse("Data collection task enqueued successfully!")
