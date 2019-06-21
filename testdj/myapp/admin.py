from django.contrib import admin
#站点管理
# Register your models here.
from .models import Grades, Students
# 界面管理
class GradesAdmin(admin.ModelAdmin):
    #列表属性
    list_display = ['pk','gname','ggirlnum','gboynum','gdate', 'isDelete']
    # list_filter = []
    list_per_page = 5
    #增加修改
    #顺序
    # fields = []
    #分组
    fieldsets = [
        ("num", {"fields":['ggirlnum' , 'gboynum']}),
        ("othoers",{"fields":['gname','gdate','isDelete']}),
    ]
#注册
admin.site.register(Grades, GradesAdmin)
admin.site.register(Students)