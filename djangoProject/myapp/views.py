import os

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


def demo(request):
    # 构建柱形图数据
    x_data = ["A", "B", "C", "D", "E"]
    y_data = [10, 20, 30, 40, 50]

    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("柱形图", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="柱形图示例"))
    )

    # 获取当前文件的绝对路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    # 构建静态文件夹的绝对路径
    static_path = os.path.join(current_path, '../static')
    # 构建要保存的图像文件的绝对路径
    image_path = os.path.join(static_path, 'bar.png')
    # 生成静态图片
    make_snapshot(snapshot, bar.render(), image_path)

    return render(request, 'demo.html')


def index(request):
    return render(request, '../templates/index.html')


from django.shortcuts import render
from .class_definition import LoginForm
from django.db import connection

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # 获取表单字段值
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 进行账户密码筛查或验证
            # 例如，可以使用Django的认证系统进行验证
            from django.contrib.auth import authenticate, login
            user = authenticate(request, username=username, password=password)

            # 或是通过筛查数据库进行
            with connection.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) FROM users WHERE username=%s AND password=%s', [username, password])
                row = cursor.fetchone()

                if row[0] > 0:
                    # 验证成功
                    return render(request, 'success.html')
                else:
                    # 验证失败
                    error_message = '用户名或密码不正确'
                    return render(request, 'index.html', {'error_message': error_message})

    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form})