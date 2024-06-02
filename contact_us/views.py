from django.shortcuts import (render, redirect)
from django.views import View
from django.http import JsonResponse
import json
from .models import ContactUs


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact_us/contact-us.html')

    def post(self, request):
        data = json.loads(request.body)

        ContactUs.objects.create(
            name=data['contact_name'],
            number=data['contact_number'],
            message=data['contact_message']
        )
        return JsonResponse({'status :': 'allright'})
