from django.http import HttpResponse
from django.template.loader import render_to_string


def robots_txt(request):
    content = render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    content = render_to_string("sitemap.xml")
    return HttpResponse(content, content_type="application/xml")
