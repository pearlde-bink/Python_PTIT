class Rectangle:
    def __init__(self, dai, rong, colo):
        self.dai = dai
        self.rong = rong
        self.colo = colo
        
    def perimeter(self):
        return self.dai * 2 + self.rong * 2
    def area(self):
        return self.dai * self.rong
    def color(self):
        s = self.colo[0].upper() + self.colo[1:].lower()
        return s
    

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    
    # arr = input().split() 
    # if int(arr[0]) > 0 and int(arr[1]) > 0: 
    #     r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    #     print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
    # else: print("INVALID")