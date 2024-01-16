from django.shortcuts import render
import razorpay
from .models import Kulfi, Payment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount")) * 100
        client = razorpay.Client(auth=("key_id", "key_secret"))
        razorpay_order = client.order.create({ 
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1"
        })
        razorpay_order["name"] = name
        # print(razorpay_order)
        kulfi = Kulfi(name = name, amount = amount, payment_id = razorpay_order["id"])
        kulfi.save()
        return render(request, 'app/index.html', {"razorpay_order": razorpay_order})

    return render(request, 'app/index.html')



@csrf_exempt
def success(request):
    if request.method == "POST":
        # print(request.POST)
        order_id = request.POST.get("razorpay_order_id")
        order = Kulfi.objects.filter(payment_id = order_id).first()
        if order:
            order.paid = True
            order.save()

            payment_id = request.POST.get("razorpay_payment_id")
            order_id = request.POST.get("razorpay_order_id")
            signature = request.POST.get("razorpay_signature")
            payment = Payment(payment_id=payment_id, order_id = order_id, signature = signature)
            payment.save()
            
        return render(request, 'app/success.html')
    return render(request, 'app/success.html')
