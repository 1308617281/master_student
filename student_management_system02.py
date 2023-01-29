from dataclasses import dataclass, field
from typing import List
# 成员变量属性
# 方法
# Python 类型注解
# Python 数据类dataclasS
# python封装与property装饰器
# 编写学员实体类，对应属性包含：学号、姓名、性别。
# 编写学员名单管理类，实现删除学员方法、查询学员方法。
# 学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
# 实现更新学员、添加学员操作。
# 根据示例代码中的注释信息，完成此题目的代码逻辑。
@dataclass
class Student:
    # pass
    cno:int#学号
    name:str#姓名
    sex:str#性别
    __grade:int=field(default=0,init=False)#成绩
    @property
    def grade(self):
        return  self.__grade
    @grade.setter
    def grade(self,value):
            if 0<= value <= 100:
                self.__grade=value
                print(f"---成绩修改信息成功，具体成绩为{value}---")
            else:
                print("输入的成绩格式有误")
class StudentList:
    def __init__(self, student_list: List[Student]):
        self.s_list = student_list

    def get(self, student_id: int):
        """
        根据 student_id 查询信息
        """
        # pass
        b = len(self.s_list)
        for a in range(0,b):
            c= [self.s_list[a].cno,self.s_list[a].name,self.s_list[a].sex]
            if student_id in c:
                print(f'---查询信息为:{c},查询完毕---')
                break
        else:
            print("----该student_id不存在--")
        # pass
    def delete(self, student_id: int):
        """
        根据 student_id 删除信息
        """
        pass
        li = []
        b = len(self.s_list)
        for a in range(0, b):
            c = [self.s_list[a].cno, self.s_list[a].name, self.s_list[a].sex]
            li.append(c)
            if student_id in c:
                li.remove(c)
                print(f'---删除信息为:{c},已删除---')
                break
        else:
            print("----该student_id不存在--")
    def update(self, student: Student):
        # pass
        '''
        #更新学员成绩
        '''
        b = len(self.s_list)
        for a in range(0, b):
            c = [self.s_list[a].cno, self.s_list[a].name, self.s_list[a].sex]
            if student.cno in c and student.name in c and student.sex in c:
                d =Student(self.s_list[a].cno, self.s_list[a].name, self.s_list[a].sex)
                # print(d.grade)#查看该学生的成绩
                #修改学生的成绩
                d.grade=80
                break
        else:
            print(f"该{student}不存在")

    def save(self, student: Student):
        # pass
        '''
        添加成员信息
        '''
        li = []
        b = len(self.s_list)
        for a in range(0, b):
            c = [self.s_list[a].cno, self.s_list[a].name, self.s_list[a].sex]
            li.append(c)
        c = [student.cno, student.name, student.sex]
        li.append(c)
        print(f"---添加信息成功，信息为{c}; 添加信息成功后，查看所有信息为{li}---")
if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(cno=1,name='lisi',sex='男')
    s2 = Student(cno=2,name='lili',sex='男')
    s3 = Student(cno=3,name='xiaoxiao',sex='女')
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    #实现save
    s_list.save(Student(cno=4,name='yaoyao',sex='女'))
    # 实现update
    s_list.update(Student(cno=1,name='lisi',sex='男'))
    # 实现get()方法
    s_list.get(2)
    # # 实现delete
    s_list.delete(3)