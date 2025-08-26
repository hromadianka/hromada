from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WikiNode, WikiEdit
from django.utils.translation import get_language
from django.urls import reverse
from django.contrib import messages
from django.db.models import Prefetch
from django.utils.translation import gettext as _

# Create your views here.

def wiki(request):
    selected_language = get_language()

    children_qs = WikiNode.objects.filter(
        is_moderated=True,
        language=selected_language,
    ).order_by('order', 'created_at')

    nodes = (
        WikiNode.objects
        .filter(parent=None, language=selected_language, is_moderated=True)
        .prefetch_related(Prefetch('children', queryset=children_qs, to_attr='visible_children'))
    )

    return render(request, 'wiki.html', {'nodes': nodes})

def wiki_edit(request, node_id):
    selected_language = get_language()
    node = get_object_or_404(WikiNode, id=node_id)
    children = node.get_children()

    if request.method == "POST":
        proposed_content = request.POST.get(f"proposed_content_{node.id}", "").strip()

        if not proposed_content:
            return JsonResponse({"success": False, "error": _("Content cannot be empty")}, status=400)

        WikiEdit.objects.create(
            node=node,
            language=selected_language,
            proposed_content=proposed_content,
            author=request.user if request.user.is_authenticated else None
        )

        for child in children:
            child_content = request.POST.get(f"proposed_content_{child.id}", "").strip()
            if child_content:
                WikiEdit.objects.create(
                    node=child,
                    proposed_content=child_content,
                    author=request.user if request.user.is_authenticated else None
                )

        return JsonResponse({"success": True})

    return render(request, "wiki_edit.html", {"node": node, "children": children})

def wiki_add(request, parent_id=None):
    parent = None
    selected_language = get_language()
    if parent_id:
        parent = get_object_or_404(WikiNode, id=parent_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if not content:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": _("Content cannot be empty")}, status=400)
            messages.error(request, _("Content cannot be empty"))
            return redirect("wiki")

        try:
            new_node = WikiNode.objects.create(
                content=content,
                parent=parent,
                author=request.user if request.user.is_authenticated else None,
                language=selected_language,
            )

            WikiEdit.objects.create(
                node=new_node,
                proposed_content=content,
                author=request.user if request.user.is_authenticated else None,
                language=selected_language,
            )

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})

            messages.success(request, _("Your edits have been submitted for moderation!"))
            return redirect("wiki")

        except Exception as e:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "error": str(e)}, status=500)
            messages.error(request, _("Something went wrong"))
            return redirect("wiki")

    return render(request, "wiki_add.html", {
        "parent": parent,
        "parent_url": parent_id and reverse('wiki_add_child', kwargs={'parent_id': parent_id}) or reverse('wiki_add'),
    })




