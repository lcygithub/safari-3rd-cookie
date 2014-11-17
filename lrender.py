#!/usr/bin/python
#-*coding:utf-8*-

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import json


def lrender(tpl=None, auth=False, staff=False):
    def func(f):
        def infunc(req, *args, **kwargs):
            if auth and not req.user.is_authenticated():
                return HttpResponseRedirect(settings.LOGIN_URL +
                    '?next=' + req.path)
            if staff and not req.user.is_staff:
                raise Http404
            r = f(req, *args, **kwargs)
            if isinstance(r, HttpResponse):
                return r
            elif tpl and 'template' not in r:
                return render_to_response(tpl, RequestContext(req, r))
            else:
                return render_to_response(
                    r.pop('template'), RequestContext(req, r))
        return infunc
    if callable(tpl):
        return func(tpl)
    return func


def ensure_staff(func):
    def infunc(request, *argv, **kwargv):
        if not request.user.is_staff:
            raise Http404
        else:
            return func(request, *argv, **kwargv)
    return infunc


class JError(Exception):
    pass


def tojson(auth=True, staff=False, method=None, need_page=False):
    def func(f):
        def infunc(req, *args, **kwargs):
            if method is not None:
                if req.method != method:
                    return HttpResponse(u'{"error": "invalid http method"}',
                        'application/json')
            if auth and not req.user.is_authenticated():
                return HttpResponse(u'{"error": "login first"}',
                    'application/json')
            if staff and not req.user.is_staff:
                return HttpResponse(u'{"error": "staff required"}',
                    'application/json')
            if need_page:
                page = req.GET.get('page', '1')
                if not all([x.isdigit() for x in page]):
                    return HttpResponse(u'{"error": "invalid page"}',
                        'application/json')
                kwargs['page'] = int(page)
            try:
                r = f(req, *args, **kwargs)
            except JError, e:
                return HttpResponse(
                    '{"error": ' + json.dumps(unicode(e)) + '}',
                    'application/json')
            if isinstance(r, bool):
                r = {'ok': r}
            elif r == None:
                r = {}
            return HttpResponse(json.dumps(r), 'application/json')
        return infunc
    if callable(auth):
        return func(auth)
    return func