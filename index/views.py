import json

from django.shortcuts import render,HttpResponse,redirect
from .models import *
import re
from django.core import serializers

# Create your views here.

def index_views(request):
    uid = request.session.get('uid')
    if uid:
        categorys = Category.objects.all()
        uid = request.session['uid']
        uid = User.objects.get(id=uid)
        films = uid.films_set.all()
        films_1 = uid.films_set.all()[0:3]
        films_2 = uid.films_set.all()[3:5]
        L = []
        for f in films:
            l = []
            l.append(f)
            info = f.info_set.all()
            for i in info:
                print('info遍历后的已阅读次数%s'%i.read_number)
            l.append(info)
            reply = f.reply_set.all()
            l.append(reply)
            L.append(l)
        return render(request,'index.html',locals())
    else:
        categorys = Category.objects.all()
        for ca in categorys:
            print(ca.category)
        films = Films.objects.all()
        films_1 = Films.objects.all()[0:3]
        films_2 = Films.objects.all()[3:5]
        film_3 = Films.objects.get(id=2)
        L = []
        for f in films:
            l = []
            l.append(f)
            info = f.info_set.all()
            for i in info:
                print('info遍历后的已阅读次数%s'%i.read_number)
            l.append(info)
            reply = f.reply_set.all()
            l.append(reply)
            L.append(l)
        return render(request,'index.html',locals())


# 注册
def register_views(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uname =request.POST.get('uname')
        email = request.POST.get('email')
        uphone = request.POST.get('uphone')
        password = request.POST.get('password')
        au = User()
        au.uname = uname
        au.uphone = uphone
        au.upwd = password
        au.email = email
        au.save()
        return redirect('/index/')


# 检查登录信息是否存在
def check_register_views(request):
    uphone = request.GET.get('uphone')
    uphone=User.objects.filter(uphone=uphone).first()
    uname = request.GET.get('uname')
    uname = User.objects.filter(uname=uname).first()
    email = request.GET.get('email')
    email = User.objects.filter(email=email).first()
    if uphone or uname or email:
        dic = {
            'static':1,
            'msg' :'已存在'
        }
    else:
        dic = {
            'status':0,
            'msg':'通过',
            }
    return HttpResponse(json.dumps(dic))


# 登录
def login_views(request):
    if request.method == "GET":
        url = request.META.get('HTTP_REFERER','/')
        if 'uid' in request.session and 'uname' in request.session:
            return redirect(url)
        else:
            if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
                uid = request.COOKIES['uid']
                uname = request.COOKIES['uname']
                request.session = uid
                request.session = uname
                return redirect(url)
            else:
                resp = render(request,'login.html',locals())
                resp.set_cookie('url',url)
                return resp
    else:
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        user = User.objects.filter(uname=uname,upwd=upwd)
        if user:
            id =user[0].id
            request.session['uid'] = id
            request.session['uname'] = uname
            resp = redirect('/')
            if 'uid' in request.POST:
                expires = 60*60*24*366
                resp.set_cookie('uid',id,expires)
                resp.set_cookie('uname',uname,expires)
            return resp
        else:
            return redirect('/login/')


# 检查是否是登录状态
def check_login_views(request):
    if 'uid' in request.session and 'uname' in request.session:
        id = request.session.get('uid')
        uname = User.objects.get(id=id).uname
        dic = {
            'loginStatus':1,
            'uname':uname,
        }
    elif 'uid' in request.COOKIES and 'uname' in request.COOKIES:
        uid = request.COOKIES['uid']
        uname = request.COOKIES['uname']
        request.session['uid'] = uid
        request.session['uid'] = uname
        dic = {
            'loginStatus': 1,
            'uname': uname,
        }
    else:
        dic ={
            'loginStatus':0
        }
    return HttpResponse(json.dumps(dic))


# 退出登录
def logout_views(request):
    if 'uid' in request.session and 'uname' in request.session:
        del request.session['uid']
        del request.session['uname']
        url = request.META.get('HTTP_REFERER','/')
        resp = redirect(url)
        if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
            resp.delete_cookie('uid')
            resp.delete_cookie('uname')
        return resp
    return redirect('/')

# 发表
def release_views(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request,'release.html',locals())
    else:
        uid = request.session['uid']
        film = request.POST.get('film')
        picture = request.POST.get('picture')
        show_date = request.POST.get('show_date')
        director = request.POST.get('director')
        stars = request.POST.get('stars')
        screenwriter = request.POST.get('screenwriter')
        type = request.POST.get('type')
        long_time = request.POST.get('long_time')
        movie_score = request.POST.get('movie_score')
        content = request.POST.get('content')
        category = request.POST.get('category')
        f = Films()
        f.film = film
        f.picture = picture
        f.show_data = show_date
        f.director = director
        f.screenwriter = screenwriter
        f.stars = stars
        f.type = type
        f.long_time = long_time
        f.movie_score = movie_score
        f.synopsis = content
        f.category_id = category
        print('category%s'%f.category)
        f.save()
        return redirect('/release/')

# 信息展示
def info_views(request):
    url = request.get_full_path()
    print('当前地址是%s'%url)
    # / info /?id = 1
    p = re.compile('\d', re.S)
    r = p.findall(url)
    r = int(r[0])
    film = Films.objects.get(id = r)
    # user_id =Films.objects.get()
    info = film.info_set.all()
    for i in info :
        print('已阅读数%s'%i.read_number)
    reply = film.reply_set.all()
    return render(request,'info.html',locals())


def gbook_views(request):
    return render(request,'gbook.html')


def header_views(request):
    return render(request,'header.html')


def list_views(request):
    return render(request,'list.html')


def photo_views(request):
    return render(request,'photo.html')


def list_views(request):
    return render(request,'list.html')


def about_views(request):
    return render(request,'about.html')