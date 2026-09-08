from pathlib import Path

from django.shortcuts import redirect, render

from .models import Post


ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
}


def feed(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        description = request.POST.get("description")
        uploaded_file = request.FILES.get("image")

        if not uploaded_file:

            error = "Please upload an image."

        else:

            extension = Path(
                uploaded_file.name
            ).suffix.lower()

            if extension not in ALLOWED_EXTENSIONS:

                error = (
                    "Only JPG, JPEG, and PNG "
                    "files are allowed."
                )

            else:

                Post.objects.create(
                    username=username,
                    description=description,
                    image=uploaded_file,
                )

                return redirect("posts:feed")

    posts = Post.objects.all().order_by("-id")

    context = {
        "posts": posts,
        "error": error,
    }

    return render(
        request,
        "feed.html",
        context,
    )


def like_post(request, post_id):

    if request.method == "POST":

        post = Post.objects.get(
            id=post_id
        )

        post.likes += 1

        post.save()

    return redirect("posts:feed")
