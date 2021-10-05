from django.urls import path
from . import views

app_name="g_pigeon_race"
urlpatterns = [
    path('', views.index, name="index"),
    path("<int:race_id>", views.race, name="race"),
    path("<int:race_id>/entry", views.entry, name="entry"),
    path("entry", views.entry2, name="entry2"),
    path("<int:race_id>/remove", views.remove, name='remove'),
    path('lap/<int:race_id>', views.lap, name="lap"),
    path("lap/lap_pigeon/<int:rd>", views.lap_pigeon, name="lap_pigeon"),
    path("loadpigeon/<int:pid>", views.load_pigeon, name="load_pigeon"),
    path("clock/", views.clock_it, name="clock"),
    path("release/<int:id>", views.release_it, name="release"),
    path("view_loaded/<int:id>", views.view_loaded, name="view_loaded"),
    path("view_loaded_dead/<int:id>", views.view_loaded_dead, name="view_loaded_dead"),
    path("view_codes/", views.view_codes, name="view_codes"),
    path("view_registered_pigeons/<int:race_id>", views.race_registered, name="races_registered"),
    #path("view_record", views.view_record, name="view_record"),
    path("clocked_lap/<int:lid>", views.view_clocked, name="view_clocked"),
    path("add_lap", views.add_lap, name="add_lap"),
    path("add_point", views.add_point, name="add_point"),
    path("manager_x", views.manager, name="manager_page"),
    path("measure_x", views.measure, name="measure"),
    path("<str:csrf_token>/create_race", views.start_race, name="start_race"),
    path("<str:csrf_token>/add_code", views.add_code, name="add_code"),

    path("start/<str:rid>", views.started_race, name="started_race"),
    path("end/<str:rid>", views.ended_race, name="ended_race"),

    path("<str:id>/View_Race_Record", views.view_race_record, name="view_race_record"),
    path("get_race_record", views.get_race_record, name="get_race_record2"),
    path("get_name/", views.get_name, name="get_name")

]
