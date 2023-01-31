# 项目简介
# 随着学校的规模变大，对应的学员回越来越多，相应的管理越来越难。 学员信息管理系统主要是对学员的各种信息进行管理，能够让学员的信息关系变得科学化、系统化和规范化。
#
# 知识点
# 实体类
# 成员变量属性
# 方法
# Python 类型注解
# Python 数据类dataclass
# python封装与property装饰器
# 文件处理
# 异常类
# venv 环境管理
# pip 环境管理
# 受众
# 高级测试工程师
# 作业要求
# 编写学员实体类，对应属性包含：学号、姓名、性别。
# 编写学员名单管理类，实现删除学员方法、查询学员方法。
# 学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
# 实现更新学员、添加学员操作。
# 添加学员时，把学员信息写入文件中；查看学员时，读取文件中学员的信息。
# 自定义异常类：添加学员传入参数不合理时抛出自定义异常。
# 创建一个venv 环境，实现环境隔离。
import json
import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    # pass
    cno: int  # 学号
    name: str  # 姓名
    sex: str  # 性别
    __grade: int = field(default=0, init=False)  # 成绩

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
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
        # student_id = int(input("请输入查询的student_id:"))#后面主方法中的s_list.get()必须传参数，没必要在这输入student_id
        # 读取data.txt文件的数据
        with open('./student.txt', "r", encoding="utf-8") as f:
            data = f.read()
            data1 = json.loads(data)  # 转换为python对象
            for a in data1:
                if student_id in a:
                    print(f'---查询信息为:{a},查询完毕---')
                    break
            else:
                print("----该student_id不存在--")
        # pass

    def delete(self, student_id: int):
        """
        根据 student_id 删除信息
        """
        # pass
        # student_id = int(input("请输入查询的student_id:"))#后面s_list.get()必须传参数，没必要在让人输入student_id
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
                d = Student(self.s_list[a].cno, self.s_list[a].name, self.s_list[a].sex)
                # 修改学生的成绩
                try:
                    d.grade = float(input("请输入修改学生的成绩为:"))  # 控制台输入学生的成绩
                    # d.grade=random.randint(0,101)#生成一个1~100之间的随机数的随机数
                except:
                    print("你修改的成绩的类型有误")
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
        print(f"---添加信息成功，信息为{c}---")
        # 将添加的学员信息写入student.txt文件内中
        with open('./student.txt', 'w+', encoding='utf-8') as f:
            f.write(json.dumps(li, ensure_ascii=False))


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(cno=1, name='lisi', sex='男')
    s2 = Student(cno=2, name='lili', sex='男')
    s3 = Student(cno=3, name='xiaoxiao', sex='女')
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现save
    try:
        s_list.save(Student(4, 'yaoyao', '女'))  # 传入正常的参数
        s_list.save(Student(5, 'yao', '女', 6))  # 参入异常的参数
    except Exception as e:
        print(f"参入的参数异常：{e}")
    # 实现update
    s_list.update(Student(cno=1, name='lisi', sex='男'))
    # 实现get()方法
    s_list.get(1)
    # # 实现delete
    s_list.delete(3)

