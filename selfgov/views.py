from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.utils.translation import gettext as _

from selfgov.models import (
    Soviet,
    SovietType,
)


def selfgov_list(request):
    all_selfgovs = Soviet.objects.filter(moderated=True)
    all_selfgovs_types = SovietType.objects.all()

    context = {
        "selfgovs": all_selfgovs,
        "selfgovs_types": all_selfgovs_types,
    }

    return render(request, "selfgov_list.html", context)


def selfgov_detail(request, selfgov_id):
    selfgov = get_object_or_404(Soviet, id=selfgov_id)
    return render(request, "selfgov_detail.html", {"selfgov": selfgov})


@login_required
def selfgov_create(request):
    all_selfgovs_types = SovietType.objects.all()

    context = {
        "selfgovs_types": all_selfgovs_types,
    }

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        chat_link = request.POST.get("chat_link", "").strip()

        soviet_type_id = request.POST.get("soviet_type")

        def parse_coord(value, min_v, max_v):
            try:
                v = float(value)
                return v if min_v <= v <= max_v else None
            except (TypeError, ValueError):
                return None

        latitude = parse_coord(request.POST.get("latitude"), -90, 90)
        longitude = parse_coord(request.POST.get("longitude"), -180, 180)

        selfgov = Soviet.objects.create(
            author=request.user if request.user.is_authenticated else None,
            title=title,
            description=description,
            chat_link=chat_link,
            soviet_type_id=soviet_type_id,
            latitude=latitude,
            longitude=longitude,
        )

        return redirect("selfgov_list")

    return render(request, "selfgov_create.html", context)


@login_required
def selfgov_edit(request, selfgov_id):
    selfgov = get_object_or_404(Soviet, id=selfgov_id)

    all_selfgovs_types = SovietType.objects.all()

    if selfgov.author != request.user:
        return HttpResponseForbidden(_("You are not allowed to edit this project"))
    else:
        if request.method == "POST":
            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            chat_link = request.POST.get("chat_link", "").strip()

            soviet_type_id = request.POST.get("soviet_type")

            def parse_coord(value, min_v, max_v):
                try:
                    v = float(value)
                    return v if min_v <= v <= max_v else None
                except (TypeError, ValueError):
                    return None

            latitude = parse_coord(request.POST.get("latitude"), -90, 90)
            longitude = parse_coord(request.POST.get("longitude"), -180, 180)

            if title:
                selfgov.title = title
                selfgov.description = description
                selfgov.chat_link = chat_link
                selfgov.soviet_type_id = soviet_type_id
                selfgov.latitude = latitude
                selfgov.longitude = longitude
                selfgov.save()

                return redirect("selfgov_detail", selfgov_id=selfgov.id)

        context = {
            "selfgov": selfgov,
            "selfgovs_types": all_selfgovs_types,
        }

        return render(request, "selfgov_edit.html", context)
