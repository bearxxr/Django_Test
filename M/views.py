from django.db.models import Sum, Max, Min, Avg, F, Q
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.cache import cache_control

from M.models import Person, Order, Custom, Grade, Student, Company


def test(request):
    return HttpResponse('test')

@cache_control(timeout=30)
def getone(request):
    # person = Person.objects.first()
    # person = Person.objects.last()
    # person = Person.objects.latest('-id')

    # 必须在有排序的结果中才有用
    persons = Person.objects.order_by('age').reverse()

    # distinct
    '''在MySQL中用不了'''

    print(type(persons))

    for person in persons:
        print(person.name, person.age)
    return HttpResponse('查询成功')


def addorder(request):
    order = Order()
    order.save()
    return HttpResponse('添加成功')


def getyear(request):
    order = Order.objects.filter(o_time__year=2020)[0]
    print(order.o_time)
    return HttpResponse('添加成功')


def getmonth(request):
    order = Order.objects.filter(o_time__month=7)[0]
    print(order.o_time)
    return HttpResponse('查询成功')


def getaggr(request):
    sum_cost = Custom.objects.aggregate(Sum("cost"))
    print(sum_cost)

    max_cost = Custom.objects.aggregate(Max("cost"))
    print(max_cost)

    min_cost = Custom.objects.aggregate(Min("cost"))
    print(min_cost)

    avg_cost = Custom.objects.aggregate(Avg("cost"))
    print(avg_cost)

    return HttpResponse('查询成功')


def getstudents(request):
    grade = Grade.objects.filter(name='python')[0]
    students = grade.student_set.all()
    print(type(students))
    for student in students:
        print(student.name)
    return HttpResponse('查询成功')


def testF(request):
    company_list = Company.objects.filter(girl_num__gt=F('boy_num'))
    for company in company_list:
        print(company.name)
    return HttpResponse('查询成功')


def testQ(request):
    # company_list = Company.objects.filter(girl_num__gt=10).filter(boy_num__gt=10)
    # for company in company_list:
    #     print(company.name)

    company_list = Company.objects.filter(Q(girl_num__gt=10) & Q(boy_num__gt=10))
    for company in company_list:
        print(company.name)

    companys = Company.objects.filter(~Q(girl_num__lte=10))
    for company in companys:
        print(company.id,company.name)


    return HttpResponse('查询成功')
