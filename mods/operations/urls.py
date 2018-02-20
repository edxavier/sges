from django.conf.urls import  url
from django.contrib.auth.decorators import login_required
from .reports import IncidentPDF, WorkaroundPDF, ChangePDF
from django.urls import path

conf_patterns = [
    path('incidents/pdf/<int:id>/', IncidentPDF.as_view()),
    path('workaround/pdf/<int:w_id>/', WorkaroundPDF.as_view()),
    path('changes/pdf/<int:c_id>/', ChangePDF.as_view()),

]