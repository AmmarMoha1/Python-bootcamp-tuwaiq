from django.shortcuts import render
from django.views import View


class DashboardHomeView(View):
    def get(self, request):
        return render(request, "dashboard_home.html")


def reports(request):
    print(request.method)

    return render(request, "reports.html")
