from weasyprint import HTML
from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from shared.Helpers import url_fetcher
from django.views.generic import View
from .models import *

class IncidentPDF(View):
    def get(self, request, id, *args, **kwargs):
        incident = get_object_or_404(Incident, pk=id)
        template = get_template("incident_detail.html")
        html = template.render(locals(), request)
        response = HttpResponse(content_type="application/pdf")
        HTML(string=html, url_fetcher=url_fetcher).write_pdf(response)
        return response


class WorkaroundPDF(View):

    def get(self, request, w_id, *args, **kwargs):
        workaround = get_object_or_404(KnownErrors, pk=w_id)
        template = get_template("workaround.html")
        html = template.render(locals(), request)
        response = HttpResponse(content_type="application/pdf")
        HTML(string=html, url_fetcher=url_fetcher).write_pdf(response)
        return response

class ChangePDF(View):

    def get(self, request, c_id, *args, **kwargs):
        change = get_object_or_404(Change, pk=c_id)
        template = get_template("change_detail.html")
        html = template.render(locals(), request)
        response = HttpResponse(content_type="application/pdf")
        HTML(string=html, url_fetcher=url_fetcher).write_pdf(response)
        return response