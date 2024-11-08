from django.urls import path
from.import views

urlpatterns=[
     path("",views.index),
     path("about/",views.about),
     path("contacts/",views.contacts),
     path("sign_in/",views.sign_in),
     path("sign_up/",views.sign_up),
     path("check_login/",views.check_login),
     path("admin_homepage/",views.admin_homepage),
     path("courses/",views.courses),
     path("add_courses/",views.add_courses),
     path("save_courses/",views.save_courses),
     path("edit_courses/<id>",views.edit_courses),
     path("update_courses/<id>",views.update_courses),
     path("delete_courses/<id>",views.delete_courses),
     path("teachers/",views.teachers),
     path("add_teachers/",views.add_teachers),
     path("save_teachers/",views.save_teachers),
     path("edit_teachers/<id>",views.edit_teachers),
     path("update_teachers/<id>",views.update_teachers),
     path("delete_teachers/<id>",views.delete_teachers),
     path("course_details/",views.course_details),
     path("application_form/<id>", views.application_form),
     path("save_application/<id>",views.save_application),
     path("teacher/",views.teacher),
     path("summary/<id>",views.summary,name="summary"),
     path("payment_handler/",views.payment_handler)















]












