'''
Demonstrates basic use of the Student class and its methods. Simple object oriented programming example.
'''
from Student import Student

if __name__=='__main__':
    s1 = Student('Smith', 'John')
    s2 = Student('Doe', 'Jane')
    
    print(s1.id_num)

    s2.set_classes(['Math', 'Science', 'History'])
    s2.print_classes()