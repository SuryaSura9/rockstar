class Time:      
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
    
    def __add__(self, other_time):
        new_time = Time()
        new_time.second = (self.second + other_time.second) % 60
        new_time.minute = (self.minute + other_time.minute) % 60 + (self.second + other_time.second)//60
        new_time.hour = (self.hour + other_time.hour) % 24 + (self.minute + other_time.minute) // 60
        return new_time
    
    def __sub__(self, other_time):
        new_time = Time()
        new_time.hour = (self.hour - other_time.hour) % 24 + (self.minute - other_time.minute) // 60
        new_time.minute = (self.minute - other_time.minute) % 60 + (self.second - other_time.second) // 60
        new_time.second = (self.second - other_time.second) % 60
        return new_time
    
def main(h1,m1,s1,h2,m2,s2):
    time1 = Time(h1, m1, s1)
    time2 = Time(h2, m2, s2)
    print(f'    1 = {time1}')
    print(f'    2 = {time2}')
    print(f'1 + 2 = {time1 + time2}')
    print(f'2 - 1 = {time2 - time1}')

def h():
    return random.randint(0,23)
    
def m():
    return random.randint(0,59)
    
for _ in range(10):
    main(h(),m(),m(),h(),m(),m())