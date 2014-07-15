from django.conf.urls import patterns, url
from kitchen import views

urlpatterns = patterns('',
        url(r'^$', views.index, name="index"),
        url(r'^login/$', views.user_login, name="login"),
        url(r'^logout/$', views.user_logout, name="logout"),
        url(r'^register/$', views.user_register, name="register"),
        url(r'^add_ingredient/$', views.add_ingredient, name="add ingredient"),
        url(r'^add_recipe/$', views.add_recipe, name="add recipe"),
        url(r'^browse_recipes/$', views.browse_recipes, name="browse recipes"),
        url(r'^shopping_list/$', views.shopping_list, name="shopping list"),
        url(r'^what_make/$', views.what_make, name="what make"),
)
