from django.shortcuts import render
import qrcode
import os
import random
import string
# from myapp.models import Qrcode_model  

def main(request):
    if request.method == "GET":
        return render(request, 'main.html', {'QRCodeDemo': True})
    elif request.method == "POST":
        url = request.POST.get('url')
        qr_code = qrcode.make(url)

        # characters = string.ascii_letters + string.digits
        # random_string = ''.join(random.choice(characters) for _ in range(10))
        # qr_code.save(f"static/{random_string}.png")
        # image = f'{random_string}.png'
        
        qr_code.save(f"static/qrcode.png")
        image = 'qrcode.png'
        
        return render(request, 'main.html', {'QRCode': True, 'image':image})
