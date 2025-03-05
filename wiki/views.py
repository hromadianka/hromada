from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WikiNode, WikiEdit
from django.utils.translation import get_language

# Create your views here.

def wiki(request):
    selected_language = get_language()
    nodes = WikiNode.objects.filter(parent=None, language=selected_language).prefetch_related('children')
    return render(request, 'wiki.html', {'nodes': nodes})

def wiki_edit(request, node_id):
    selected_language = get_language()
    node = get_object_or_404(WikiNode, id=node_id)
    children = node.get_children()

    if request.method == "POST":
        proposed_content = request.POST.get(f"proposed_content_{node.id}", "").strip()

        if not proposed_content:
            return JsonResponse({"success": False, "error": "Content cannot be empty"}, status=400)

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