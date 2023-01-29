# 编写学员实体类，对应属性包含：学号、姓名、性别。
# 编写学员名单管理类，实现删除学员方法、查询学员方法。# 根据示例代码中的注释信息，完成此题目的代码逻辑。
class Student:
    def __init__(self,cno,name,sex):
        self.cno=cno
        self.name=name
        self.sex=sex
class StudentList:
    def __init__(self, student_list):
        self.s_list = student_list
        # print(student_list[0].name,student_list[1].cno,student_list[2].sex)
    def get(self, student_id):
        # student_id=int(input("请输入查询的student_id:"))
        b=len(self.s_list)
        for a in range(0,b):
            c= [self.s_list[a].cno,self.s_list[a].name,self.s_list[a].sex]
            if student_id in c:
                print(f'---查询信息为:{c},查询完毕---')
                break
        else:
            print("----该student_id不存在--")
        # pass
    def delete(self, student_id):
        # student_id = int(input("请输入查询的student_id:"))
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
    # pass
if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1,"lili","女")
    s2 = Student(2,"xiaoming","男")
    s3 = Student(3,"lisi","男")
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现get()方法
    s_list.get(3)#查询一个存在的学生
    s_list.get(4)#查询一个不存在的学生
    # 实现delete
    s_list.delete(2)#删除一个存在的学生信息
    s_list.delete(4)#删除一个存在的学生信息


