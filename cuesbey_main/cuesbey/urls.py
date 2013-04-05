from django.conf.urls import patterns, url, include
from django.contrib import admin

from cuesbey_main.cube_diff.views import (card_contents, poll_state,
                                          available_heuristics)

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^djangular/', include('djangular.urls')),
                       url(r'^card_contents/?$', card_contents),
                       url(r'^heuristics/?$', available_heuristics),
                       url(r'^poll_state/$', poll_state, name="poll_state"),
)