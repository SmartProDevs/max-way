from django.shortcuts import render

def main_dashboard(request):
    return render(request, 'dashboard/index.html')

