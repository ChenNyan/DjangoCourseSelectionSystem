from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from students.models import User, Teacher, Student, Course, course_student, Score


# Create your views here.

def index(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'index.html')


def register(request):
    if request.session.get('is_login', None):
        return render(request, 'index.html')
    if request.method == "POST":
        message = "请检查填写的内容！"
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        real_name = request.POST.get('relname', '')
        id = request.POST.get('id', '')
        kind = request.POST.get('kind', '')
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'register.html', {"error":"两次密码不同", "message":message})
        else:
            same_name_user = User.objects.filter(name=username)
            if same_name_user:  # 用户名唯一
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'register.html', {"error":"两次密码不同", "message":message})
            # 当一切都OK的情况下，创建新用户
            new_user = User.objects.create()
            new_user.name = username
            new_user.password = password1
            new_user.kind = kind
            new_user.save()
            if kind == 'teacher':
                new_tea = Teacher.objects.create(id_id=new_user.id)
                new_tea.teacherName = real_name
                new_tea.teacherID = id
                new_tea.save()
            else:
                new_stu = Student.objects.create(id_id=new_user.id)
                new_stu.id_id = new_user.id
                new_stu.studentName = real_name
                new_stu.studentID = id
                new_stu.save()
            return render(request, 'index.html')  # 自动跳转到登录页面
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(name=username)
        if user:
            user = User.objects.get(name=username)
            if password == user.password:
                request.session['IS_LOGIN'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                if user.kind == 'teacher':
                    id = request.session.get("user_id")
                    tea = Teacher.objects.get(id=id)
                    name = tea.teacherName
                    courses = Course.objects.filter(courseTeacher=id)
                    return render(request, 'index_tea.html', {'name':name, 'courses':courses})
                if user.kind =='admin':
                    return render(request, 'index_adm.html')
                else:
                    id = request.session.get("user_id")
                    stu = Student.objects.get(id=id)
                    name = stu.studentName
                    courses = Course.objects.filter(courseStudent=id)
                    return render(request, 'index_stu.html', {'name': name, 'courses':courses})
            else:
                return render(request, 'index.html', {'error': '密码错误!'})
        else:
            return render(request, 'index.html', {'error': '用户不存在!'})
    else:
        return render(request, 'index.html')


def logout(request):
    if not request.session.get('IS_LOGIN', None):
        return redirect("/index/")
    del request.session['IS_LOGIN']
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/index/')


def tea1(request):
    return render(request, 'tea1.html')


def newcou(request):
    if request.method == 'POST':
        coursename = request.POST.get('coursename', '')
        coursecredit = request.POST.get('coursecredit', '')
        id = request.session['user_id']
        new_cou = Course()
        new_cou.courseName = coursename
        new_cou.courseCredit = coursecredit
        new_cou.courseTeacher_id = id
        new_cou.save()
        tea = Teacher.objects.get(id=id)
        name = tea.teacherName
        courses = Course.objects.filter(courseTeacher=id)
        return render(request, 'index_tea.html', {'name': name, 'courses': courses})


def stu1(request):
    allcou = Course.objects.all()
    return render(request, 'stu1.html', {'allcou':allcou})


def getcou(request):
    if request.method == 'POST':
        couid = request.POST.get('couid', '')
        stuid = request.session['user_id']
        cou = get_object_or_404(Course, id=couid)
        cou.save()
        cou.courseStudent.add(stuid)
        stu = Student.objects.get(id=stuid)
        name = stu.studentName
        courses = Course.objects.filter(courseStudent=stuid)
        return render(request, 'index_stu.html', {'name': name, 'courses': courses})


def score(request):
    teaid = request.session['user_id']
    courses = Course.objects.filter(courseTeacher=teaid)
    return render(request, 'score.html', {'courses':courses})


def score_stu(request, pk):
    cs = course_student.objects.filter(course=pk)
    course = get_object_or_404(Course, id=pk)
    students = Student.objects.all()
    return render(request, 'score_stu.html', {'course':course, 'cs':cs, 'students':students})


def scoreinfo(request, pk1, pk2):
    course = get_object_or_404(Course, id=pk1)
    student = get_object_or_404(Student, id_id=pk2)
    return render(request, 'scoreinfo.html', {'course':course, 'student':student})


def setsco(request, pk1, pk2):
    if request.method == 'POST':
        sco = request.POST.get('sco', '')
        cre = request.POST.get('cre', '')
        couid = pk1
        stuid = pk2
        newsco = Score()
        newsco.scoreStudent_id = stuid
        newsco.scoreCourse = couid
        newsco.scoreDate = sco
        newsco.scoreCredit = cre
        newsco.save()
        return HttpResponse('登记成功')


def stusco(request):
    stuid = request.session['user_id']
    cs = course_student.objects.filter(student_id=stuid)
    allcou = Course.objects.all()
    return render(request, 'stusco.html', {'cs':cs, 'allcou':allcou})


def stuscoinfo(request, pk1, pk2):
    sco = get_object_or_404(Score, scoreStudent=pk1, scoreCourse=pk2)
    allcou = Course.objects.all()
    pk3 = int(pk2)
    return render(request, 'stuscoinfo.html', {'sco':sco, 'allcou':allcou, 'pk3':pk3})