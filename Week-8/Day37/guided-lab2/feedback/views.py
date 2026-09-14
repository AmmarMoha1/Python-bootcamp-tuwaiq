from django.shortcuts import redirect, render

from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            return redirect(
                "feedback:thank_you"
            )

    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "feedback/contact.html",
        context,
    )


def thank_you(request):
    return render(
        request,
        "feedback/thank_you.html",
    )
    