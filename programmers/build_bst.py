# 먼저 노드 클래스를 생성한다. (해당 클래스는 검색알고리즘에 필요한 기본클래스이다.)
class Node:
    def __init__(self, value): 
      self.value = value
      self.left = None #왼쪽 서브노드
      self.right = None #오른쪽 서브노드
class BinarySearchTree:
    def __init__(self, head): #BinarySearchTree 클래스 생성자
        self.head = head #부모 노드
    
    #노드 삽입 메소드
    def insert_node(self, value):
        self.base_node = self.head #연산의 기준 노드 변수 선언
        while True:
            if self.base_node.value > value: #기준 노드 값이 삽입하고자 하는 값보다 큰 경우 (삽입 값은 좌측 노드로 내려간다)
                if self.base_node.left != None: #기준 노드의 좌측 자식노드가 존재한다면
                    self.base_node = self.base_node.left #다음 연산을 위해 기준노드를 좌측 자식노드로 초기화
                else: #기준 노드의 좌측 자식노드가 존재하지 않는다면
                    self.base_node.left = Node(value) #좌측 자식노드에 값 삽입
                    break
            else: #기준 노드 값이 삽입하고자 하는 값보다 작은 경우
                if self.base_node.right != None: #기준 노드의 우측 자식노드가 존재한다면
                    self.base_node = self.base_node.right #다음 연산을 위해 기준노드를 우측 자식노드로 초기화
                else: #기준 노드의 우측 자식노드가 존재하지 않는다면
                    self.base_node.right = Node(value) #우측 자식노드에 값 삽입
                    break
	
    #노드 검색 메소드
    def search_node(self, value):
        self.base_node = self.head #연산의 기준 노드 변수 선언
        
        while self.base_node: #기준 노드가 존재하는 동안
            if self.base_node.value == value: #기준 노드의 값이 검색하고자 하는 값과 같다면
                return True #True 반환
                break
            
            elif self.base_node.value > value: #기준 노드의 값이 검색하고자 하는 값보다 클 때
                if self.base_node.left != None: #기준 노드의 좌측 자식노드가 존재한다면
                    self.base_node = self.base_node.left #다음 연산을 위해 기준 노드를 좌측 자식노드로 초기화
                else: #기준 노드의 좌측 자식노드가 없다면
                    return False #False 반환(검색하고자 하는 값이 없음)
            
            elif self.base_node.value < value: #기준 노드의 값이 검색하고자 하는 값보다 작을 때
                if self.base_node.right != None: #기준 노드의 우측 자식노드가 존재한다면
                    self.base_node = self.base_node.right #다음 연산을 위해 기준 노드를 우측 자식노드로 초기화
                else: #기준 노드의 우측 자식노드가 없다면
                    return False #False 반환(검색하고자 하는 값이 없음)


head = Node(16) #Node 클래스 객체 생성 (root == 16)
bt = BinarySearchTree(head) #BinarySearchTree 클래스 객체 생성 (root == 16)
bt.insert_node(12) # 값이 12인 노드 삽입
bt.insert_node(19) # 값이 19인 노드 삽입
bt.insert_node(11) # 값이 11인 노드 삽입
bt.insert_node(13) # 값이 13인 노드 삽입
bt.insert_node(18) # 값이 18인 노드 삽입
bt.insert_node(20) # 값이 20인 노드 삽입
bt.insert_node(9) # 값이 9인 노드 삽입
bt.insert_node(8) # 값이 8인 노드 삽입
bt.insert_node(10) # 값이 10인 노드 삽입
print(bt.search_node(5))    #False
print(bt.search_node(-2))   #False
print(bt.search_node(18))   #True


# if __name__ == "__main__":
#     result = insert_node(1)
#     print(result)
#     # [[1]]

#     result = insert_node(2)
#     print(result)
#     # [[1, '*', 2], [2, 1]]

#     result = insert_node(3)
#     print(result)
#     # [[1, '*', 2, '*', 3], [1, '*', 3, 2], [2, 1, 3], [3, 1, '*', '*', 2], [3, 2, '*', 1]]
