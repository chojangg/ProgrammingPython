#클래스 변수: 객체로 생성 하지 않아도 클래스에 하나 존재하는 변수
#클래스 메소드: 객체로 생성 하지 않아도 클래스에 하나 존재하는 메소드

# 학생
# 속성 : 학번, 이름
class Student:
    def __init__(self, student_number, name):
        self.student_number = student_number
        self.name = name

    def __str__(self):
        return f'학번 : {self.student_number}\t이름 : {self.name}'


# 동아리
# 속성 : 동아리명, 장소, 멤버들
# 메소드 : 장소 설정하자(), 멤버 추가하자(), 활동하자()
class Club:
    count = 0

    @classmethod
    def get_count_club(cls):
        return f'동아리 개수 : {Club.count}'

    def __init__(self, name):
        self.name = name
        self.location = None
        self.members = []
        Club.count += 1

    def __str__(self):
        s = ''
        for member in self.members:
            s += str(member) + "\t"
        return f'동아리명 : {self.name}\t장소 : {self.location}\t멤버들 : {s}'

    def set_location(self, location):
        self.location = location

    def add_member(self, student):
        self.members.append(student);

    def set_action(self, action):
        self.action = action

    def act(self):
        print(self.action)


학생1 = Student('2213', '임채영')
print(학생1)
학생2 = Student('2106', '양다연')
print(학생2)

동아리1 = Club("사진반")
동아리1.set_location('실습1')
동아리1.set_action("사진 찍기")
동아리1.add_member(학생2)
동아리1.add_member(학생1)
print(동아리1)
동아리1.act()
print(len(동아리1.members))

동아리2 = Club("c언어 알고리즘반")
동아리2.set_action("코딩하기")
동아리2.add_member(학생2)
print(동아리2)
동아리2.act()

print(Club.count)
print(Club.get_count_club())