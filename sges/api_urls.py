from django.conf.urls import url, include
from rest_framework import routers
from mods.users import views
from mods.schedule import views as schedule_view
from mods.catalogs import views as catalog_vset
from mods.operations import views as ope_vset

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

router.register(r'catalogs/forms_data', catalog_vset.FormsViewSet, base_name='forms_data')
router.register(r'catalogs/items', catalog_vset.ItemViewSet)
router.register(r'catalogs/services', catalog_vset.ServiceViewSet)
router.register(r'catalogs/item_history', catalog_vset.ItemHistoryViewSet)

router.register(r'operations/incidents', ope_vset.IncidentViewSet)
router.register(r'operations/incident_entries', ope_vset.IncidentEntryViewSet)
router.register(r'operations/incidents-forms-data', ope_vset.FormsViewSet, base_name='incidents-forms-data')
router.register(r'operations/incidents-resume', ope_vset.IncidentResumeViewSet, base_name='incidents-resume')

router.register(r'operations/tasks', ope_vset.TaskViewSet, base_name='tasks')
router.register(r'operations/tasks_entries', ope_vset.TaskEntryViewSet)
router.register(r'operations/tasks-forms-data', ope_vset.TaskFormsViewSet, base_name='task-forms-data')

router.register(r'operations/changes', ope_vset.ChangeViewSet, base_name='changes')
router.register(r'operations/changes_entries', ope_vset.ChangeEntryViewSet)


router.register(r'operations/workarounds', ope_vset.WorkaroundViewSet)


router.register(r'schedule/rol', schedule_view.RolViewSet)
router.register(r'schedule/matrix', schedule_view.MatrixViewSet)
router.register(r'schedule/employe_rols', schedule_view.EmployeRolViewSet)


