
from django import http
from django.views.generic.base import View
from django.core.cache import cache

class Index(View):

    def get(self, request):
        data = cache.get('xxx')

        if not data:
            print "calculating data!!!"
            data = "THIS IS MY DATA!!!!"
            cache.set('xxx', data)

        return http.HttpResponse(data)
