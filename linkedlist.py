
class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def set_next(self, next):
        self.__next = next

    def set_prev(self, prev):
        self.__prev = prev

    def next(self):
        return self.__next

    def prev(self):
        return self.__prev

    def __repr__(self):
        return str(self.__data)


class LinkedList:
    def __init__(self, data=None):
        # 적절히 구현하시오.
        #self.__head = Node()
        #self.__tail = Node()
        #self.__next = None
        #data는 list 타입으로 가정함
        self.__head = Node()
        self.__tail = Node()
        self.__next = self.__head
        self.__head.set_next(self.__tail)
        self.__tail.set_prev(self.__head)
        if data is not None:    #data가 들어있는 경우를 안해서 추가
            for i in data:
                self.append(i)

    def empty(self):
        if self.__head.next() == self.__tail:
            return True
        else:
            return False

    def size(self):
        #다른사람꺼 보고 더 깔끔하게
        cnt = 0
        cur = self.__head
        while cur.next() is not self.__tail:
            cur = cur.next()
            cnt += 1
        return cnt
        #cur_node = self.__head
        #cnt = -2
        #while cur_node is not None: ##head->tail , tail->None 이렇게 총 2번
        #    cur_node = cur_node.next()
        #    cnt += 1
        #return cnt

    def head(self):
        return self.__head.next()   #난 head랑 tail을 None으로 잡고 할꺼니까 head는 .__head 다음꺼야!

    def tail(self):
        return self.__tail.prev()

    def appendleft(self, data):
        return self.insert(None, data)

    def append(self, data):
        return self.insert(self.__tail, data)

    def insert(self, cur_node, data):
        if cur_node is self.__tail:
            prev_node = self.__tail.prev()
            new_node = Node(prev_node,self.__tail,data)
            self.__tail.set_prev(new_node)
            prev_node.set_next(new_node)
        else:
            if cur_node is None:
                cur_node = self.__head
            next_node = cur_node.next()
            new_node = Node(cur_node,next_node,data)
            cur_node.set_next(new_node)
            next_node.set_prev(new_node)
        return new_node                 ##테스트 케이스보면 cur_node에 node를 집어넣는데 그거 떄문에 넣어줌

    def remove(self, cur_node):
        if cur_node is None or self.empty() or cur_node == self.__head: # head면 아무동작 안하는거
            return cur_node                 ##pass로 하니까 insert처럼 테스트케이스의 cur_node에 node를 할당하는 연산이 없음
        if cur_node == self.__tail:
            cur_node = cur_node.prev()
        prev_node = cur_node.prev()
        next_node = cur_node.next()
        prev_node.set_next(next_node)
        next_node.set_prev(prev_node)
        del cur_node
        return next_node


    def next(self, cur_node):
        if cur_node is None:
            pass
        elif cur_node.next() == self.__tail:
            return cur_node
        else:
            return cur_node.next()

    def prev(self, cur_node):
        if cur_node is None:
            pass
        elif cur_node.prev() == self.__head:
            return self.__head
        else:
            return cur_node.prev()

    def __len__(self):
        return self.size()

    def __repr__(self):
        cur_node = self.__head.next()
        elements = []
        while cur_node is not None and cur_node.next():
            elements.append(str(cur_node))
            cur_node = cur_node.next()
        return str(elements)

    def __iter__(self):
        self.__next = self.__head.next()
        return self

    def __next__(self):
        if self.__next is not None and\
                self.__next.next():
            next_node = self.__next
            self.__next = self.__next.next()
            return next_node
        else: raise StopIteration