# from lrender import lrender, tojson
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import json

# @lrender("aindex.html")
def index(req):
	response = render_to_response('index.html', {}, context_instance=RequestContext(req))
	response.set_cookie("target", "target cookie ")
	# response.set_cookie("target", "target cookie ", max_age=None, expires=None, path='/', secure=None, httponly=False);
	response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
	return response


def set_cookie(req):
	response = HttpResponseRedirect("http://dianpu.tmall.com?iscookie")
	# response = render_to_response('cookie.html', {}, context_instance=RequestContext(req))
	# response.set_cookie("cookie_proxy", "proxy cookie ")
	# response.set_cookie("cookie_proxy", "proxy cookie ", max_age=None, expires=None, path='/', secure=None, httponly=False);
	response.set_cookie("cookie_proxy", "proxy cookie ", max_age=None, expires=None, domain="game.play.jaeapp.com", path='/', secure=None, httponly=False);
	# response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
	return response

def cookie(req):
	print "cookie"
	print req
	response = HttpResponse(u'{"success": "lcyang"}','application/json')
	response['Access-Control-Allow-Origin'] = "http://dianpu.tmall.com"
	response['Access-Control-Allow-Credentials'] = 'true'
	response['Access-Control-Allow-Methods'] = 'POST,GET'
	response['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type, withCredentials,set-cookie'
	response.set_cookie("async-cookie", "ajax-set-cookie",max_age=None, expires=None, path='/', secure=None, httponly=False)
	response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
	return response

def dianpu(req):
	response = render_to_response('dianpu.html', {}, context_instance=RequestContext(req))
	response.set_cookie("dianpu", "dianpu cookie ", max_age=None, expires=None, path='/', secure=None, httponly=False);
	return response

def window_open(req):
	response = render_to_response('modaldialog.html', {}, context_instance=RequestContext(req))
	# response.set_cookie("dianpu", "dianpu cookie ", max_age=None, expires=None, path='/', secure=None, httponly=False);
	return response


def dialog(req):
	response = render_to_response('dialog.html', {}, context_instance=RequestContext(req))
	response.set_cookie("dialog-cookie", "dialog-set-cookie",max_age=None, expires=None, path='/', secure=None, httponly=False)
	response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
	return response

def open_cookie(req):
	response = render_to_response('open_cookie.html',{}, context_instance=RequestContext(req))
	response.set_cookie("cookie_proxy", "proxy cookie ", max_age=None, expires=None, path='/', secure=None, httponly=False);
	return response