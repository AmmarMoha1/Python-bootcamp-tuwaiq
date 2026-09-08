from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def upload_profile(request):

    image_url = None

    if request.method == "POST":

        uploaded_file = request.FILES.get("avatar")

        if uploaded_file:

            storage = FileSystemStorage()

            filename = storage.save(
                uploaded_file.name,
                uploaded_file,
            )

            image_url = storage.url(filename)

    context = {
        "image_url": image_url,
    }

    return render(
        request,
        "profile.html",
        context,
    )
