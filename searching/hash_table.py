class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List() :
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)

    def search(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def print_LL(self):
        temp = self.head
        if not temp:
            print(None)
        while temp:
            if temp.next:
                print(temp.value, "--->", end = " ")
            else:
                print(temp.value)
            temp = temp.next
    


class Hash_table():
    def __init__(self, size):
        self.size = size
        self.hashtable = [None]*self.size  # 사이즈의 크기 만큼 해시테이블을 만들어 준다.
        for x in range(self.size) : 
            self.hashtable[x] = Linked_List()  # 각각의 공간에 링크드 리스트를 만들어 준다.

    def hash(self, key):
        # hash function is h(x) = x%10
        return key % 10

    def insert_key(self, key):
        index = self.hash(key)  # index로 값을 받아온다.
        self.hashtable[index].insert(key)  # hashtable이 링크드리스트이므로 작동한다.

    def search_key(self, key):
        index = self.hash(key)
        boolean = self.hashtable[index].search(key)
        return boolean

    def print_HT(self):
        print("Hash table is :- \n")
        print("Index \t\t Values\n")
        for x in range(self.size):
            # print(x, end="\t\t")
            self.hashtable[x].print_LL()


HT = Hash_table(10)
HT.insert_key(10)  #10 은 나머지가 0 이므로 인덱스가 0으로 들어감
HT.insert_key(90)  #90 도 나머지가 0 이므로 10과 연결됨
HT.insert_key(25)  #25 는 나머지가 5 이므로 5로 들어감
HT.insert_key(5)   #5  도 나머지가 5 이므로 5로 들어감 (25와 연결)
HT.insert_key(35)  #35 도 나머지가 5 이므로 5로 들어감 (5와 연결)
HT.insert_key(27)  #27 은 나머지가 7 이므로 7로 들어감
HT.insert_key(17)  #17 도 나머지가 7 이므로 7로 들어감 (27과 연결)
HT.insert_key(22)  #22 는 나머지가 2 이므로 2로 들어감
if HT.search_key(17):   #17을 찾아달라
    print("Given key is present\n")
else:
    print("Given key is not present\n")
HT.print_HT()

# 빈공간이 많은데, 이것이 해시테이블의 특징임