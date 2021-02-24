from django.db import models

# Create your models here.
class User(models.Model):
    attribute = (
        ('teacher', '教师'),
        ('student', '学生'),
        ('admin', '管理员')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    kind = models.CharField(max_length=10, choices=attribute, default='学生')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Teacher(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacherID = models.CharField(max_length=20)
    teacherName = models.CharField(max_length=20, null=True)


class Student(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentID = models.CharField(max_length=20)
    studentName = models.CharField(max_length=20)
    studentCredit = models.IntegerField(null=True)


class Admin(models.Model):
    id = models.OneToOneField(User,models.CASCADE,primary_key=True)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=20)
    courseCredit = models.CharField(max_length=20)
    courseTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    courseStudent = models.ManyToManyField(Student, through='course_student')


class Score(models.Model):
    id = models.AutoField(primary_key=True)
    scoreStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    scoreDate = models.IntegerField(null=True)
    scoreCourse = models.IntegerField(null=True)
    scoreCredit = models.CharField(max_length=20)


class course_student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)