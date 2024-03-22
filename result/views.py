# pylint: disable-all
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from accounts.models import User, Student
from app.models import Session, Semester
from course.models import Course
from accounts.decorators import lecturer_required, student_required
from .models import TakenCourse, Result

# pdf
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    LongTable,
)
from reportlab.lib.styles import getSampleStyleSheet, black, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus.tables import Table
from reportlab.lib.units import inch
from reportlab.lib import colors
from .models import *

cm = 2.54

now = datetime.now()
now = datetime.now()
# ########################################################
# Score Add & Add for
# ########################################################
@login_required
@lecturer_required
def add_score(request):
    """
    Shows a page where a lecturer will select a course allocated to him for score entry.
    in a specific semester and session

    """
    current_session = Session.objects.get(is_current_session=True)
    current_semester = get_object_or_404(
        Semester, is_current_semester=True, session=current_session
    )
    # semester = Course.objects.filter(allocated_course__lecturer__pk=request.user.id, semester=current_semester)
    courses = Course.objects.filter(
        allocated_course__lecturer__pk=request.user.id
    ).filter(semester=current_semester)
    context = {
        "current_session": current_session,
        "current_semester": current_semester,
        "courses": courses,
    }
    return render(request, "result/add_score.html", context)


@login_required
@lecturer_required
def add_score_for(request, id):
    """
    Shows a page where a lecturer will add score for students that are taking courses allocated to him
    in a specific semester and session
    """
    current_session = Session.objects.get(is_current_session=True)
    current_semester = get_object_or_404(
        Semester, is_current_semester=True, session=current_session
    )
    if request.method == "GET":
        courses = Course.objects.filter(
            allocated_course__lecturer__pk=request.user.id
        ).filter(semester=current_semester)
        course = Course.objects.get(pk=id)
        # myclass = Class.objects.get(lecturer__pk=request.user.id)
        # myclass = get_object_or_404(Class, lecturer__pk=request.user.id)

        # students = TakenCourse.objects.filter(course__allocated_course__lecturer__pk=request.user.id).filter(
        #     course__id=id).filter(student__allocated_student__lecturer__pk=request.user.id).filter(
        #         course__semester=current_semester)
        students = (
            TakenCourse.objects.filter(
                course__allocated_course__lecturer__pk=request.user.id
            )
            .filter(course__id=id)
            .filter(course__semester=current_semester)
        )
        context = {
            "title": "Submit Score | ESYSTEM ",
            "courses": courses,
            "course": course,
            # "myclass": myclass,
            "students": students,
            "current_session": current_session,
            "current_semester": current_semester,
        }
        return render(request, "result/add_score_for.html", context)

    if request.method == "POST":
        ids = ()
        data = request.POST.copy()
        data.pop("csrfmiddlewaretoken", None)  # remove csrf_token
        for key in data.keys():
            ids = ids + (
                str(key),
            )  # gather all the all students id (i.e the keys) in a tuple
        for s in range(
            0, len(ids)
        ):  # iterate over the list of student ids gathered above
            student = TakenCourse.objects.get(id=ids[s])
            # print(student)
            # print(student.student)
            # print(student.student.department.id)
            courses = (
                Course.objects.filter(level=student.student.level)
                .filter(program__pk=student.student.department.id)
                .filter(semester=current_semester)
            )  # all courses of a specific level in current semester
            total_credit_in_semester = 0
            for i in courses:
                if i == courses.count():
                    break
                else:
                    total_credit_in_semester += int(i.credit)
            score = data.getlist(
                ids[s]
            )  # get list of score for current student in the loop
            assignment = score[
                0
            ]  # subscript the list to get the fisrt value > ca score
            mid_exam = score[1]  # do the same for exam score
            quiz = score[2]
            attendance = score[3]
            marks_1 = score[4]
            marks_2 = score[5]
            marks_3 = score[6]
            marks_4= score[7]
            marks_5 = score[8]
            marks_6 = score[9]
            marks_7 = score[10]
            marks_8= score[11]
            marks_9 = score[12]
            marks_10= score[13]
            
            marks_11 = score[14]
            marks_12 = score[15]
            marks_13 = score[16]
            marks_14= score[17]
            marks_15 = score[18]
            marks_16 = score[19]
            marks_17 = score[20]
            marks_18= score[21]
            marks_19 = score[22]
            marks_20= score[23]
            
            marks_21 = score[24]
            marks_22 = score[25]
            marks_23 = score[26]
            marks_24= score[27]
            marks_25 = score[28]
            marks_26 = score[29]
            marks_27 = score[30]
            marks_28= score[31]
            marks_29 = score[32]
            marks_30= score[33]
            
            marks_31 = score[34]
            marks_32 = score[35]
            marks_33 = score[36]
            marks_34= score[37]
            marks_35 = score[38]
            marks_36 = score[39]
            marks_37 = score[40]
            marks_38= score[41]
            marks_39 = score[42]
            marks_40= score[43]
            
            marks_41 = score[44]
            marks_42 = score[45]
            marks_43 = score[46]
            marks_44= score[47]
            marks_45 = score[48]
            marks_46 = score[49]
            marks_47 = score[50]
            marks_48= score[51]
            marks_49 = score[52]
            marks_50= score[53]
            final_exam = score[44]
            obj = TakenCourse.objects.get(pk=ids[s])  # get the current student data
            obj.assignment = assignment  # set current student assignment score
            obj.mid_exam = mid_exam  # set current student mid_exam score
            obj.quiz = quiz  # set current student quiz score
            obj.attendance = attendance  # set current student attendance score
            obj.marks_1 = marks_1
            obj.marks_2 = marks_2
            obj.marks_3 = marks_3
            obj.marks_4 = marks_4
            obj.marks_5 = marks_5
            obj.marks_6 = marks_6
            obj.marks_7 = marks_7
            obj.marks_8 = marks_8
            obj.marks_9 = marks_9
            obj.marks_10 = marks_10
            
            obj.marks_11 = marks_11
            obj.marks_12 = marks_12
            obj.marks_13 = marks_13
            obj.marks_14 = marks_14
            obj.marks_15 = marks_15
            obj.marks_16 = marks_16
            obj.marks_17 = marks_17
            obj.marks_18 = marks_18
            obj.marks_19 = marks_19
            obj.marks_20 = marks_20
            
            obj.marks_21 = marks_21
            obj.marks_22 = marks_22
            obj.marks_23 = marks_23
            obj.marks_24 = marks_24
            obj.marks_25 = marks_25
            obj.marks_26 = marks_26
            obj.marks_27 = marks_27
            obj.marks_28 = marks_28
            obj.marks_29 = marks_29
            obj.marks_30 = marks_30
            
            
            obj.marks_31 = marks_31
            obj.marks_32 = marks_32
            obj.marks_33 = marks_33
            obj.marks_34 = marks_34
            obj.marks_35 = marks_35
            obj.marks_36 = marks_36
            obj.marks_37 = marks_37
            obj.marks_38 = marks_38
            obj.marks_39 = marks_39
            obj.marks_40 = marks_40
            
            obj.marks_41 = marks_41
            obj.marks_42 = marks_42
            obj.marks_43 = marks_43
            obj.marks_44 = marks_44
            obj.marks_45 = marks_45
            obj.marks_46 = marks_46
            obj.marks_47 = marks_47
            obj.marks_48 = marks_48
            obj.marks_49 = marks_49
            obj.marks_50 = marks_50
            obj.final_exam = final_exam  # set current student final_exam score

            obj.total = obj.get_total(
                assignment=assignment,
                mid_exam=mid_exam,
                quiz=quiz,
                attendance=attendance,
                marks_1=marks_1,
                marks_2=marks_2,
                marks_3=marks_3,
                marks_4=marks_4,
                marks_5=marks_5,
                marks_6=marks_6,
                marks_7=marks_7,
                marks_8=marks_8,
                marks_9=marks_9,
                marks_10=marks_10,
                
                marks_11=marks_11,
                marks_12=marks_12,
                marks_13=marks_13,
                marks_14=marks_14,
                marks_15=marks_15,
                marks_16=marks_16,
                marks_17=marks_17,
                marks_18=marks_18,
                marks_19=marks_19,
                marks_20=marks_20,
                
                marks_21=marks_21,
                marks_22=marks_22,
                marks_23=marks_23,
                marks_24=marks_24,
                marks_25=marks_25,
                marks_26=marks_26,
                marks_27=marks_27,
                marks_28=marks_28,
                marks_29=marks_29,
                marks_30=marks_30,
                
                marks_31=marks_31,
                marks_32=marks_32,
                marks_33=marks_33,
                marks_34=marks_34,
                marks_35=marks_35,
                marks_36=marks_36,
                marks_37=marks_37,
                marks_38=marks_38,
                marks_39=marks_39,
                marks_40=marks_40,
                
                marks_41=marks_41,
                marks_42=marks_42,
                marks_43=marks_43,
                marks_44=marks_44,
                marks_45=marks_45,
                marks_46=marks_36,
                marks_47=marks_47,
                marks_48=marks_48,
                marks_49=marks_49,
                marks_50=marks_50,
                final_exam=final_exam,
            )
            obj.grade = obj.get_grade(total=obj.total)

            # obj.total = obj.get_total(assignment, mid_exam, quiz, attendance, final_exam)
            # obj.grade = obj.get_grade(assignment, mid_exam, quiz, attendance, final_exam)

            obj.point = obj.get_point(grade=obj.grade)

            obj.comment = obj.get_comment(grade=obj.grade)
            # obj.carry_over(obj.grade)
            # obj.is_repeating()
            obj.save()
            gpa = obj.calculate_gpa(total_credit_in_semester)
            cgpa = obj.calculate_cgpa()

            try:
                a = Result.objects.get(
                    student=student.student,
                    semester=current_semester,
                    session=current_session,
                    level=student.student.level,
                )
                a.gpa = gpa
                a.cgpa = cgpa
                a.save()
            except:
                Result.objects.get_or_create(
                    student=student.student,
                    gpa=gpa,
                    semester=current_semester,
                    session=current_session,
                    level=student.student.level,
                )

            # try:
            #     a = Result.objects.get(student=student.student, semester=current_semester, level=student.student.level)
            #     a.gpa = gpa
            #     a.cgpa = cgpa
            #     a.save()
            # except:
            #     Result.objects.get_or_create(student=student.student, gpa=gpa, semester=current_semester, level=student.student.level)

        messages.success(request, "Successfully Recorded! ")
        return HttpResponseRedirect(reverse_lazy("add_score_for", kwargs={"id": id}))
    return HttpResponseRedirect(reverse_lazy("add_score_for", kwargs={"id": id}))


# ########################################################


@login_required
@student_required
def grade_result(request):
    student = Student.objects.get(student__pk=request.user.id)
    courses = TakenCourse.objects.filter(student__student__pk=request.user.id).filter(
        course__level=student.level
    )
    # total_credit_in_semester = 0
    results = Result.objects.filter(student__student__pk=request.user.id)

    result_set = set()

    for result in results:
        result_set.add(result.session)

    sorted_result = sorted(result_set)

    total_first_semester_credit = 0
    total_sec_semester_credit = 0
    for i in courses:
        if i.course.semester == "First":
            total_first_semester_credit += int(i.course.credit)
        if i.course.semester == "":
            total_sec_semester_credit += int(i.course.credit)
        if i.course.semester == "third":
            total_sec_semester_credit += int(i.course.credit)
        if i.course.semester == "fourth":
            total_sec_semester_credit += int(i.course.credit)
        if i.course.semester == "fifth":
            total_sec_semester_credit += int(i.course.credit)

    previousCGPA = 0
    # previousLEVEL = 0
    # calculate_cgpa
    for i in results:
        previousLEVEL = i.level
        try:
            a = Result.objects.get(
                student__student__pk=request.user.id,
                level=previousLEVEL,
                semester="Second",
            )
            previousCGPA = a.cgpa
            break
        except:
            previousCGPA = 0

    context = {
        "courses": courses,
        "results": results,
        "sorted_result": sorted_result,
        "student": student,
        "total_first_semester_credit": total_first_semester_credit,
        "total_sec_semester_credit": total_sec_semester_credit,
        "total_first_and_second_semester_credit": total_first_semester_credit
        + total_sec_semester_credit,
        "previousCGPA": previousCGPA,
    }

    return render(request, "result/grade_results.html", context)


@login_required
@student_required
def assessment_result(request):
    student = Student.objects.get(student__pk=request.user.id)
    courses = TakenCourse.objects.filter(
        student__student__pk=request.user.id, course__level=student.level
    )
    result = Result.objects.filter(student__student__pk=request.user.id)

    context = {
        "courses": courses,
        "result": result,
        "student": student,
    }

    return render(request, "result/assessment_results.html", context)


@login_required
@lecturer_required
def result_sheet_pdf_view(request, id):
    current_semester = Semester.objects.get(is_current_semester=True)
    current_session = Session.objects.get(is_current_session=True)
    result = TakenCourse.objects.filter(course__pk=id)
    course = get_object_or_404(Course, id=id)
    no_of_pass = TakenCourse.objects.filter(course__pk=id, comment=" "+today.strftime("%d/%m/%y")).count()
    no_of_fail = TakenCourse.objects.filter(course__pk=id, comment="* "+today.strftime("%d/%m/%y")).count()
    fname = (
        str(current_semester)
        + "_semester_"
        + str(current_session)
        + "_"
        + str(course)
        + "_resultSheet.pdf"
    )
    fname = fname.replace("/", "-")
    flocation = settings.MEDIA_ROOT + "/result_sheet/" + fname

    doc = SimpleDocTemplate(
        flocation,
        rightMargin=0,
        leftMargin=6.5 * cm,
        topMargin=0.3 * cm,
        bottomMargin=0,
    )
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(name="ParagraphTitle", fontSize=11, fontName="FreeSansBold")
    )
    Story = [Spacer(1, 0.2)]
    style = styles["Normal"]

    # picture = request.user.picture
    # l_pic = Image(picture, 1*inch, 1*inch)
    # l_pic.__setattr__("_offs_x", 200)
    # l_pic.__setattr__("_offs_y", -130)
    # Story.append(l_pic)

    # logo = settings.MEDIA_ROOT + "/logo/img/schoollogo.PNG"
    # im_logo = Image(logo, 1*inch, 1*inch)
    # im_logo.__setattr__("_offs_x", -218)
    # im_logo.__setattr__("_offs_y", -60)
    # Story.append(im_logo)

    print("\nsettings.MEDIA_ROOT", settings.MEDIA_ROOT)
    print("\nsettings.STATICFILES_DIRS[0]", settings.STATICFILES_DIRS[0])
    logo = settings.STATICFILES_DIRS[0] + "/img/schoollogo.PNG"
    im = Image(logo, 1 * inch, 1 * inch)
    im.__setattr__("_offs_x", -200)
    im.__setattr__("_offs_y", -45)
    Story.append(im)

    style = getSampleStyleSheet()
    normal = style["Normal"]
    normal.alignment = TA_CENTER
    normal.fontName = "Helvetica"
    normal.fontSize = 12
    normal.leading = 15
    title = (
        "<b> "
        + str(current_semester)
        + " Attended Register for "
        + str(current_session)
        + " PROGRAM</b>"
    )
    title = Paragraph(title.upper(), normal)
    Story.append(title)
    Story.append(Spacer(1, 0.1 * inch))

    style = getSampleStyleSheet()
    normal = style["Normal"]
    normal.alignment = TA_CENTER
    normal.fontName = "Helvetica"
    normal.fontSize = 10
    normal.leading = 15
    title = "<b>Stream/Subject Instructor: " + request.user.get_full_name + "</b>"
    title = Paragraph(title.upper(), normal)
    Story.append(title)
    Story.append(Spacer(1, 0.1 * inch))

    normal = style["Normal"]
    normal.alignment = TA_CENTER
    normal.fontName = "Helvetica"
    normal.fontSize = 10
    normal.leading = 15
    level = result.filter(course_id=id).first()
    title = "<b>Level: </b>" + str(level.course.level)
    title = Paragraph(title.upper(), normal)
    Story.append(title)
    Story.append(Spacer(1, 0.6 * inch))

    elements = []
    count = 0
    header = [("N/S","ID NO.","Full Name", "Attendance(%)","Date")]
    

    table_header = Table(header, [1.2 * inch], [0.5 * inch])  # Increase the width by 0.2 inch
    table_header.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.black),
            ("TEXTCOLOR", (1, 0), (-1, -1), colors.white),
            ("TEXTCOLOR", (0, 0), (0, 0), colors.cyan),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.05, colors.black),
        ]
      )
      )
    Story.append(table_header)

    for student in result:
        data = [
            (
                count + 1,
                student.student.student.username.upper(),
                Paragraph(
                    student.student.student.get_full_name.capitalize(), styles["Normal"]
                ),
                student.total,
                student.comment,
                
            )
        ]
        color = colors.black
        if student.grade == "F":
            color = colors.red
        count += 1

        t_body = Table(data, colWidths=[1.2 * inch])  # Increase the width by 0.2 inches
        t_body.setStyle(
        TableStyle(
        [
            ("INNERGRID", (0, 0), (-1, -1), 0.05, colors.black),
            ("BOX", (0, 0), (-1, -1), 0.1, colors.black),
        ]
         )
           )
        Story.append(t_body)

    Story.append(Spacer(1, 1 * inch))
    style_right = ParagraphStyle(
        name="right", parent=styles["Normal"], alignment=TA_RIGHT
    )
    tbl_data = [
        [

        Paragraph("<b>Date And Time:</b>"+now.strftime("%d/%m/%Y "), styles["Normal"]),
        Paragraph("<b>No of students who attended:</b> " + str(no_of_pass), style_right),
        ],
        [
            Paragraph(
                "<b>Siganture / Stamp:</b> _________________________", 
                styles["Normal"],
               
            ),
         Paragraph("<b>No of students who did not attend:</b>" + str(no_of_fail), style_right),
        ],
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)

    doc.build(Story)

    fs = FileSystemStorage(settings.MEDIA_ROOT + "/result_sheet")
    with fs.open(fname) as pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = "inline; filename=" + fname + ""
        return response
    return response


@login_required
@student_required
def course_registration_form(request):
    """
    Generate a PDF registration form for the currently logged-in student.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: HttpResponse containing the generated PDF registration form.
    """
    # current_semester = Semester.objects.get(is_current_semester=True)
    current_session = Session.objects.get(is_current_session=True)
    courses = TakenCourse.objects.filter(student__student__id=request.user.id)
    fname = request.user.username + ".pdf"
    fname = fname.replace("/", "-")
    # flocation = '/tmp/' + fname
    # print(MEDIA_ROOT + "\\" + fname)
    flocation = settings.MEDIA_ROOT + "/registration_form/" + fname
    doc = SimpleDocTemplate(
        flocation, rightMargin=15, leftMargin=15, topMargin=0, bottomMargin=0
    )
    styles = getSampleStyleSheet()

    Story = [Spacer(1, 0.5)]
    Story.append(Spacer(1, 0.4 * inch))
    style = styles["Normal"]

    style = getSampleStyleSheet()
    normal = style["Normal"]
    normal.alignment = TA_CENTER
    normal.fontName = "Helvetica"
    normal.fontSize = 12
    normal.leading = 18
    title = "<b>NETCAMPUS UNIVERSITY OF TECHNOLOGY</b>"
    title = Paragraph(title.upper(), normal)
    Story.append(title)
    style = getSampleStyleSheet()

    school = style["Normal"]
    school.alignment = TA_CENTER
    school.fontName = "Helvetica"
    school.fontSize = 10
    school.leading = 18
    school_title = "<b>SCHOOL OF LEARNING</b>"
    school_title = Paragraph(school_title.upper(), school)
    Story.append(school_title)

    style = getSampleStyleSheet()
    Story.append(Spacer(1, 0.1 * inch))
    department = style["Normal"]
    department.alignment = TA_CENTER
    department.fontName = "Helvetica"
    department.fontSize = 9
    department.leading = 18
    department_title = "<b>DEPARTMENT OF ACCOUNTING </b>"
    department_title = Paragraph(department_title, department)
    Story.append(department_title)
    Story.append(Spacer(1, 0.3 * inch))

    title = "<b><u>PROOF OF REGISTRATION</u></b>"
    title = Paragraph(title.upper(), normal)
    Story.append(title)
    student = Student.objects.get(student__pk=request.user.id)
    

    style_right = ParagraphStyle(name="right", parent=styles["Normal"])
    tbl_data = [
        [
            Paragraph(
                "<b>Registration Number : " + request.user.username.upper() + "</b>",
                styles["Normal"],
            )
        ],
        [
            Paragraph(
                "<b>Name : " + request.user.get_full_name.upper() + "</b>",
                styles["Normal"],
            )
        ],
        [
            Paragraph(
                "<b>Session : " + current_session.session.upper() + "</b>",
                styles["Normal"],
            ),
            Paragraph("<b>Level: " + student.level + "</b>", styles["Normal"]),
        ],
    ]
    tbl = Table(tbl_data)
    Story.append(tbl)
    Story.append(Spacer(1, 0.6 * inch))

    style = getSampleStyleSheet()
    semester = style["Normal"]
    semester.alignment = TA_LEFT
    semester.fontName = "Helvetica"
    semester.fontSize = 9
    semester.leading = 18
    semester_title = "<b>FIRST SEMESTER</b>"
    semester_title = Paragraph(semester_title, semester)
    Story.append(semester_title)

    elements = []

    # FIRST SEMESTER
    count = 0
    header = [
        (
            "S/No",
            "Course Code",
            "Course Title",
            "Unit",
            Paragraph("Name, Siganture of course lecturer & Date", style["Normal"]),
        )
    ]
    table_header = Table(header, 1 * [1.4 * inch], 1 * [0.5 * inch])
    table_header.setStyle(
        TableStyle(
            [
                ("ALIGN", (-2, -2), (-2, -2), "CENTER"),
                ("VALIGN", (-2, -2), (-2, -2), "MIDDLE"),
                ("ALIGN", (1, 0), (1, 0), "CENTER"),
                ("VALIGN", (1, 0), (1, 0), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 0), "CENTER"),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("ALIGN", (-4, 0), (-4, 0), "LEFT"),
                ("VALIGN", (-4, 0), (-4, 0), "MIDDLE"),
                ("ALIGN", (-3, 0), (-3, 0), "LEFT"),
                ("VALIGN", (-3, 0), (-3, 0), "MIDDLE"),
                ("TEXTCOLOR", (0, -1), (-1, -1), colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
            ]
        )
    )
    Story.append(table_header)

    first_semester_unit = 0
    for course in courses:
        if course.course.semester == FIRST:
            first_semester_unit += int(course.course.credit)
            data = [
                (
                    count + 1,
                    course.course.code.upper(),
                    Paragraph(course.course.title, style["Normal"]),
                    course.course.credit,
                    "",
                )
            ]
            color = colors.black
            count += 1
            table_body = Table(data, 1 * [1.4 * inch], 1 * [0.3 * inch])
            table_body.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (-2, -2), (-2, -2), "CENTER"),
                        ("ALIGN", (1, 0), (1, 0), "CENTER"),
                        ("ALIGN", (0, 0), (0, 0), "CENTER"),
                        ("ALIGN", (-4, 0), (-4, 0), "LEFT"),
                        ("TEXTCOLOR", (0, -1), (-1, -1), colors.black),
                        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                        ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                    ]
                )
            )
            Story.append(table_body)

    style = getSampleStyleSheet()
    semester = style["Normal"]
    semester.alignment = TA_LEFT
    semester.fontName = "Helvetica"
    semester.fontSize = 8
    semester.leading = 18
    semester_title = (
        "<b>Total Second First Credit : " + str(first_semester_unit) + "</b>"
    )
    semester_title = Paragraph(semester_title, semester)
    Story.append(semester_title)

    # FIRST SEMESTER ENDS HERE
    Story.append(Spacer(1, 0.6 * inch))

    style = getSampleStyleSheet()
    semester = style["Normal"]
    semester.alignment = TA_LEFT
    semester.fontName = "Helvetica"
    semester.fontSize = 9
    semester.leading = 18
    
    table_header = Table(header, 1 * [1.4 * inch], 1 * [0.5 * inch])
    table_header.setStyle(
        TableStyle(
            [
                ("ALIGN", (-2, -2), (-2, -2), "CENTER"),
                ("VALIGN", (-2, -2), (-2, -2), "MIDDLE"),
                ("ALIGN", (1, 0), (1, 0), "CENTER"),
                ("VALIGN", (1, 0), (1, 0), "MIDDLE"),
                ("ALIGN", (0, 0), (0, 0), "CENTER"),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("ALIGN", (-4, 0), (-4, 0), "LEFT"),
                ("VALIGN", (-4, 0), (-4, 0), "MIDDLE"),
                ("ALIGN", (-3, 0), (-3, 0), "LEFT"),
                ("VALIGN", (-3, 0), (-3, 0), "MIDDLE"),
                ("TEXTCOLOR", (0, -1), (-1, -1), colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
            ]
        )
    )
    Story.append(table_header)

    second_semester_unit = 0
    for course in courses:
        if course.course.semester == SECOND:
            second_semester_unit += int(course.course.credit)
            data = [
                (
                    count + 1,
                    course.course.code.upper(),
                    Paragraph(course.course.title, style["Normal"]),
                    course.course.credit,
                    "",
                )
            ]
            color = colors.black
            count += 1
            table_body = Table(data, 1 * [1.4 * inch], 1 * [0.3 * inch])
            table_body.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (-2, -2), (-2, -2), "CENTER"),
                        ("ALIGN", (1, 0), (1, 0), "CENTER"),
                        ("ALIGN", (0, 0), (0, 0), "CENTER"),
                        ("ALIGN", (-4, 0), (-4, 0), "LEFT"),
                        ("TEXTCOLOR", (0, -1), (-1, -1), colors.black),
                        ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
                        ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                    ]
                )
            )
            Story.append(table_body)

    style = getSampleStyleSheet()
    semester = style["Normal"]
    semester.alignment = TA_LEFT
    semester.fontName = "Helvetica"
    semester.fontSize = 8
    semester.leading = 18
    semester_title = (
        "<b>Total Second Semester Credit : " + str(second_semester_unit) + "</b>"
    )
    semester_title = Paragraph(semester_title, semester)
    Story.append(semester_title)

    Story.append(Spacer(1, 2))
    style = getSampleStyleSheet()
    certification = style["Normal"]
    certification.alignment = TA_JUSTIFY
    certification.fontName = "Helvetica"
    certification.fontSize = 8
    certification.leading = 18
    student = Student.objects.get(student__pk=request.user.id)
    certification_text = (
        "CERTIFICATION OF REGISTRATION: I certify that <b>"
        + str(request.user.get_full_name.upper())
        + "</b>\
    has been duly registered for the <b>"
        + student.level
        + " level </b> of study in the department\
    of LEARNING HIGH SCHOOL and that the courses and credits registered are as approved by the senate of the University"
    )
    certification_text = Paragraph(certification_text, certification)
    Story.append(certification_text)
  
    # FIRST SEMESTER ENDS HERE

    # Define the default image offsets
    default_offsets = {
    0: (438, 510),
    1: (438, 510),
    2: (438, 510),
    3: (458, 520),
    4: (478, 540),
    5: (498, 560),
    6: (518, 580),
    7: (548, 615),
    8: (558, 630),
    9: (578, 650),
    10: (598, 670),
    11: (618, 700),
    12: (638, 2700),  # Update the last offset to avoid overflow
    13: (660, 2700),  # Update the last offset to avoid overflow
    14: (680, 2700),  # Update the last offset to avoid overflow
    }

    # Check if count is within the offset dictionary, otherwise use the default offset
    image_offset = default_offsets.get(count, (680, 2700))

    # Add the logo
    logo = settings.STATICFILES_DIRS[0] + "/img/schoollogo.PNG"
    im_logo = Image(logo, 1 * inch, 1 * inch)
    im_logo.__setattr__("_offs_x", -218)
    im_logo.__setattr__("_offs_y", image_offset[0])  # Use the appropriate y-offset
    Story.append(im_logo)

    # Add the user picture
    picture = settings.BASE_DIR + request.user.get_picture()
    im = Image(picture, 1.0 * inch, 1.0 * inch)
    im.__setattr__("_offs_x", 218)
    im.__setattr__("_offs_y", image_offset[1])  # Use the appropriate y-offset
    Story.append(im)


    doc.build(Story)
    fs = FileSystemStorage(settings.MEDIA_ROOT + "/registration_form")
    with fs.open(fname) as pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = "inline; filename=" + fname + ""
        return response
    return response
