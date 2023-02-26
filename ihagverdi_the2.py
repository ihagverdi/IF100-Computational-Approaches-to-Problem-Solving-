PreviousSemesterCourses= input("Please enter the courses you have taken previously with letter grades: ")
if PreviousSemesterCourses.count(":") != (PreviousSemesterCourses.count(";")+1) :
  print("Invalid input")
else:
  CurrentSemesterStringCourses = input("Please enter the courses you have taken this semester with letter grades: ")
  if CurrentSemesterStringCourses.count(":") != (CurrentSemesterStringCourses.count(";")+1) :
    print("Invalid input")
  else:
    CheckingCourse= input("Please enter the course you want to check: ")
    PreviousSemesterCourse_list = (PreviousSemesterCourses.replace(";",":")).split(":")
    CurrentSemesterCourse_list = (CurrentSemesterStringCourses.replace(";",":")).split(":")
    if  CheckingCourse not in CurrentSemesterCourse_list: 
      print("You didn't take",CheckingCourse,"this semester.")
    else:
      PositionOfGrade = (CurrentSemesterCourse_list.index(CheckingCourse)+1)
      if "F" in CurrentSemesterCourse_list[PositionOfGrade] or "f" in CurrentSemesterCourse_list[PositionOfGrade] :
        if CheckingCourse not in PreviousSemesterCourse_list :
          print("Your grade for",CheckingCourse,"is U.")
        else:
          PositionOfPreviousGrade = (PreviousSemesterCourse_list.index(CheckingCourse)+1)
          if "U" == PreviousSemesterCourse_list[PositionOfPreviousGrade] or "u" == PreviousSemesterCourse_list[PositionOfPreviousGrade] :
            print("Your grade for",CheckingCourse,"is U.")
          else:
            print("Your grade for",CheckingCourse,"is F.")
      else:
        print("You can choose between S and ",(CurrentSemesterCourse_list[PositionOfGrade]).capitalize()," for ",CheckingCourse,".",sep="")



# Hagverdi Ibrahimli
# 00030014

