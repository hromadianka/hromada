from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from selfgov.models import Soviet
from django.utils.translation import gettext as _
from django.http import HttpResponseForbidden, JsonResponse

# Create your views here.

def selfgov_list(request):
    all_selfgovs = Soviet.objects.filter(moderated=True)
    return render(request, 'selfgov_list.html', {'all_selfgovs': all_selfgovs})

def selfgov_detail(request, selfgov_id):
    selfgov = get_object_or_404(Soviet, id = selfgov_id)
    return render(request, 'selfgov_detail.html', {'selfgov': selfgov})

def selfgov_create(request):
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        chat_link = request.POST.get('chat_link', '').strip()

        try:
            soviet_type = int(request.POST.get('soviet_type'))
        except (TypeError, ValueError):
            soviet_type = Soviet.SovietType.OTHER

        def parse_coord(value, min_v, max_v):
            try:
                v = float(value)
                return v if min_v <= v <= max_v else None
            except (TypeError, ValueError):
                return None

        latitude = parse_coord(request.POST.get('latitude'), -90, 90)
        longitude = parse_coord(request.POST.get('longitude'), -180, 180)

        selfgov = Soviet.objects.create(
            author=request.user if request.user.is_authenticated else None,
            title=title,
            description=description,
            chat_link=chat_link,
            soviet_type=soviet_type,
            latitude=latitude,
            longitude=longitude,
        )

        return redirect('selfgov_list')

    return render(request, 'selfgov_create.html', {
        'soviet_types': Soviet.SovietType.choices
    })

@login_required
def selfgov_edit(request, selfgov_id):
    selfgov = get_object_or_404(Soviet, id = selfgov_id)

    if selfgov.author != request.user:
        return HttpResponseForbidden(_("You are not allowed to edit this project"))

    else:

        if request.method == 'POST':
            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            chat_link = request.POST.get('chat_link', '').strip()

            try:
                soviet_type = int(request.POST.get('soviet_type'))
                if soviet_type not in [t.value for t in Soviet.SovietType]:
                    soviet_type = selfgov.soviet_type
            except (TypeError, ValueError):
                soviet_type = selfgov.soviet_type

            def parse_coord(value, min_v, max_v):
                try:
                    v = float(value)
                    return v if min_v <= v <= max_v else None
                except (TypeError, ValueError):
                    return None

            latitude = parse_coord(request.POST.get('latitude'), -90, 90)
            longitude = parse_coord(request.POST.get('longitude'), -180, 180)

            if title:
                selfgov.title = title
                selfgov.description = description
                selfgov.chat_link = chat_link
                selfgov.soviet_type = soviet_type
                selfgov.latitude = latitude
                selfgov.longitude = longitude
                selfgov.save()

                return redirect("selfgov_detail", selfgov_id = selfgov.id)

        return render(request, 'selfgov_edit.html', {
            'selfgov': selfgov
        })
