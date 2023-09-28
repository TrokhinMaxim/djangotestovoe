from .models import Order
from customers.models import Customer


from django.shortcuts import render
from .forms import OrderForm
from robots.models import Robot


def order_robot(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_email = form.cleaned_data["customer_email"]
            robot = form.cleaned_data["robot"]
            customer, created = Customer.objects.get_or_create(email=customer_email)
            robot_available = Robot.objects.filter(serial=robot).exists()
            order = Order(
                customer=customer, robot_serial=robot, robot_available=robot_available
            )
            order.save()

            if robot_available:
                return render(request, "orders/order_success.html")
            else:
                return render(request, "orders/out_of_stock.html")
    else:
        form = OrderForm()

    return render(request, "orders/order_robot.html", {"form": form})
