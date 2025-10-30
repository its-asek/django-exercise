from django.shortcuts import render

from .services.pesel_utils import check_pesel


def home(request):
    result = ""
    if request.method == "POST":
        user_pesel = request.POST.get("user_pesel", "")
        result = check_pesel(user_pesel)
    return render(request, "pesel_decoder/main_page.html", {"result": result})
