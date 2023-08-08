from django.shortcuts import render
import qrcode

def main(request):
    if request.method == "GET":
        return render(request, 'main.html', {'QRCodeDemo': True})
    elif request.method == "POST":
        url = request.POST.get('url')
        qr_code = qrcode.make(url)

        qr_code.save("static/qrcode.png")
        image = 'qrcode.png'
        
        return render(request, 'main.html', {'QRCode': True, 'image':image})
