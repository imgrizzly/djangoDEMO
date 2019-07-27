from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django import forms
from .models import User,Order,Member
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

class Form1(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    if request.method=="POST":
        f = request.POST["username"]
        print (f)
        return HttpResponse(f+"login Success!!!")
    else:
        context = {'':'' }
        return render(request, 'login.html', context)

def login(request):
    if request.method=="POST":
        # username = request.POST["username"]
        # passwd = request.POST["password"]
        # _user_password = User.objects.get(name=username)
        return  redirect('/purchase_sale/main/')
    #     if username == _user_password.name and passwd == _user_password.password:
    #         return  render(request, 'index.html')
    # else:
    #     return HttpResponse( "login Fail!!!")

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
def main(request):
    return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html')

def orderlist(request):
    _order= Order.objects.all()

    return render(request, 'order-list.html', {'items':_order})

def orderadd(request):
    if request.method == "POST":
        orderdata = Order(
            orderName=request.POST["username"],
            orderPayee=request.POST["orderPayee"],
            orderPhone=request.POST["orderPhone"],
        )
        orderdata.save()
        return HttpResponse("")
    else:
        return render(request, 'order-add.html')

class OrderListJson(BaseDatatableView):
    order_columns = ['number', 'user', 'status']

    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
        # these are simply objects displayed in datatable
        # You should not filter data returned here by any filter values entered by user. This is because
        # we need some base queryset to count total number of records.
        return Member.objects.filter(something=self.kwargs[''])

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example
        filter_customer = self.request.GET.get('customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        json_data = []
        for item in qs:
            json_data.append([
                escape(item.number),  # escape HTML for security reasons
                escape("{0} {1}".format(item.customer_firstname, item.customer_lastname)),  # escape HTML for security reasons
                item.get_state_display(),
                item.created.strftime("%Y-%m-%d %H:%M:%S"),
                item.modified.strftime("%Y-%m-%d %H:%M:%S")
            ])
        return json_data


def memberlist(request):
    return render(request, 'member-list.html')


def memberlistdata(request):
    try:
        if request.method == "POST":
            # 获取翻页后该页要展示多少条数据。默认为10；此时要是不清楚dataTables的ajax的post返回值
            # 可以打印一下看看【print(request.POST)】
            page_length = int(request.POST.get('iDisplayLength', '15'))
            # 该字典将转化为json格式的数据返回给前端，字典中的key默认的名字不能变
            rest = {
                "iTotalRecords": page_length,  # 本次加载记录数量
            }
            # 获取传递过来的该页的起始位置，第一页的起始位置为0.
            page_start = int(request.POST.get('iDisplayStart', '0'))
            # 该页的结束位置则就是"开始的值 + 该页的长度"
            page_end = page_start + page_length
            # 开始查询数据库，只请求这两个位置之间的数据

            # // 获取到前端ajax传递过来的buildId
            # buildId = request.POST['buildId']
            # print(request.POST)
            # 数据库查询等操作
            # build = Member.objects(id=buildId).first()
            # member_list = Member.objects.filter(memberID=buildId)
            member_all = Member.objects.all()
            total_length = member_all.count()
            member_list = member_all[page_start: page_end]
            tests_info = []
            # 按实际情况做，主要是将数据库查询到的数据转化为json形式返回给前端
            for test in member_list:
                # 注意字典中的key名字要和前端的对应一致
                data = {
                    "memberID": test.memberID,
                    "memberName": test.memberName,
                    "memberGender": test.memberGender,
                    "memberPhone": test.memberPhone,
                    "memberEmail": test.memberEmail,
                    "memberAddr":test.memberAddr,
                    "memberJoinTime":test.memberJoinTime,
                    "memberStatus":test.memberStatus,
                }
                tests_info.append(data)
                rest['iTotalDisplayRecords'] = total_length
                rest['data'] = tests_info
            return HttpResponse(json.dumps(rest, cls=DjangoJSONEncoder), content_type="application/json")  #tests_info, cls=DjangoJSONEncoder
        else:
            return HttpResponse('非法请求方式')
    except Exception as e:
        return HttpResponse(e.args)

