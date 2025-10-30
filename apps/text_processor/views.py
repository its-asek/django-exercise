from django.shortcuts import render

from .services.text_utils import process_text
from .forms import TextUploadForm


def home(request):
    return render(request, "text_processor/main_page.html")


def result(request):
    if request.method == "POST":
        form = TextUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["text_file"]
            try:
                text = file.read().decode("utf-8")
            except UnicodeDecodeError:
                return render(
                    request,
                    "text_processor/result.html",
                    dict(text="Please send UTF-8 encoded text."),
                )
            processed_text = process_text(text)
            return render(
                request, "text_processor/result.html", dict(text=processed_text)
            )
        else:
            return render(
                request,
                "text_processor/result.html",
                dict(text="Please send .txt file."),
            )

    return render(request, "text_processor/result.html", dict(text="No file sent."))
