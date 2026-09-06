from django.shortcuts import render


def checkout(request):
    return render(request, "checkout.html")


def receipt(request):
    return render(request, "receipt.html")
