from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    # msg = "Hello Python"
    # return HttpResponse("Hello World !!!")

    sql = "SELECT code, created, updated, created_user, updated_user, deleted_flag, used_flag, name FROM biz_code"
    cursor = connection.cursor()
    result = cursor.execute(sql)
    codes = cursor.fetchall()
    connection.close()

    datas = []
    for code in codes:
        datas.append({"code": code[0],
                      "created": code[1],
                      "updated": code[2],
                      "created_user": code[3],
                      "updated_user": code[4],
                      "deleted_flag": code[5],
                      "used_flag": code[6],
                      "name": code[7],
                      })

    return render(request, "main.html", {"datas": datas})
