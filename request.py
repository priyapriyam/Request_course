import requests
import json
from pprint import pprint 
import pathlib

saral_url = "http://saral.navgurukul.org/api/courses"

def writting_data(file,data):
        with open(file,"w") as file1:
                file1.write (json.dumps(data))
        # file1.close()

def data_read(file):
    file=open(file,"r")
    file_read=file.read()
    data_load=json.loads(file_read)
    return (data_load)

def course(url):
        json_file="courses.json"
        filename=pathlib.Path(json_file)
        if filename.exists():
               read_data = data_read(json_file)
               return read_data                
        else:
                response = requests.get(url)
                data=response.json()
                writting_data("courses.json",data)
                return data
json_Data=course(saral_url)
coursesIdList=[]

def saral_courses(data_load):

        for index in range(len(data_load['availableCourses'])):
                courses=data_load['availableCourses'][index]
                courses_name=courses['name']
                coursesId=courses['id']
                coursesIdList.append(coursesId)
                print index+1,".",courses_name," id.",coursesId
        return coursesIdList
a=saral_courses(json_Data)
# print a

user_input=input("Enter your course id number")
# print user_input
id_num=coursesIdList[user_input-1]
# print id_num
exercise_url1= "http://saral.navgurukul.org/api/courses/"+str(id_num)+"/exercises"
# print exercise_url1

def exercise(url1):
        json_file1="exercises/exercise"+str(id_num)+".json"
        print json_file1
        filename1=pathlib.Path(json_file1)
        if filename1.exists():
              read_data1 = data_read(json_file1)
              print "file reading"
              return read_data1
        else:
                response1=requests.get(url1)
                data1=response1.json()
                print "writting file"
                writting_data(json_file1,data1)

exe_data=exercise(exercise_url1)
# print exe_data

ExerciseIdList=[]
# course_list=exercise_courses(courses)
# print course_list#
Exercise_id_list=[]
def exer_name(a):
        num=1
        for index in a["data"]:
                # print index
                exercisesName =  index["name"]
                exerciseid=index["id"]
                Exercise_id_list.append(exerciseid)
                # print Exercise_id_list

                print num,".",exercisesName
                num=num+1
                
        
                for i in index["childExercises"]:
                        print "\t",i["name"]
        return Exercise_id_list
                
allExercises = exer_name(exe_data)        
# print allExercises


user = input("enter your exercises number")
particular_exer = allExercises[user-1]
# print particular_exer
slug_list=[]
slug_id_list=[]
count=1
for index in exe_data["data"]:
        if particular_exer==index["id"]:
                print count,".",index["name"]
                child_exercise=index["childExercises"]
                Exercise_slug = index["slug"]
                slug_list.append (Exercise_slug)
                for i in child_exercise:
                        slug_list.append(i["slug"])
                        print "\t", count+1,".",i["name"]
                        slug_id_num = i["id"]
                        slug_id_list.append(slug_id_num)
                        count=count+1
print slug_id_list
# print slug_list
user_input=input("Enter the prticular exercise no.")
slug_id=slug_list[user_input-1]
content_id=slug_id_list[user_input-1]


                


saral_url1="http://saral.navgurukul.org/api/courses/"+str(id_num)+"/exercise/getBySlug?slug="+str(slug_id)
print saral_url1

def get_content(url2):
        json_file2="sulgcontent"+str(content_id)+".json"
        print json_file2
        filename2=pathlib.Path(json_file2)
        if filename2.exists():
                read_data2=data_read(json_file2)
                print "file is readable"
                return read_data2["content"]
        else:
                response2=requests.get(url2)
                data2=response2.json()
                print "writting file"
                writting_data(json_file2,data2)
        # print data2
                # return data2["content"]
content_data=get_content(saral_url1)
print content_data
user_input=raw_input("Enter the up")
if user_input=="up":
     print saral_courses(data_read())