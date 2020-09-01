from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1 import models


def say_hello(request):
    return HttpResponse("helloworld")


# 查看数据
def user_list(request):
    myalldata = models.Person.objects.all()  # 取出表中所有数据
    return render(request, 'user_list.html', {'user_list': myalldata})


# 新增数据
def add_user(request):
    error_name = ''
    if request.method == 'POST':
        # 1、获取前端输入的数据
        new_name = request.POST.get('name')
        new_context = request.POST.get('context')
        new_sex = request.POST.get('sex')
        user_list = models.Person.objects.filter(name=new_name)
        # 2、判断数据库是否存在
        if user_list:
            error_name = '%s用户名已经存在了' % new_name
            return render(request, 'add_user.html', {'error_name': error_name})
        # 3、存储到数据库中
        else:
            user = models.Person.objects.create(name=new_name, context=new_context, sex=new_sex)
            user.save()
            return redirect('/user_list/')
    return render(request, 'add_user.html')


# 删除数据
def delete_user(request):
    # 取出需要删除的id
    delete_id = request.GET.get('id')
    # 从数据库删除的
    models.Person.objects.filter(id=delete_id).delete()
    return redirect('/user_list/')


# 修改数据
def update_user(request):
    update_id = request.GET.get('id')
    if request.method == 'POST':
        new_context = request.POST.get('context')
        # 找到匹配的id
        update_obj = models.Person.objects.get(id=update_id)
        # 取出密码和新密码对应
        update_obj.context = new_context
        # 保存数据库
        update_obj.save()
        return redirect('/user_list/')
    ret = models.Person.objects.get(id=update_id)
    return render(request, 'update_user.html', {'ret': ret})
