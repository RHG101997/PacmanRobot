
class Target:
    def __init__(self, colorLower, colorUpper):
        # HSV Color space
        self.colorLower = colorLower
        self.colorUpper = colorUpper
        self.onScreen = False
    
    '''Function unpacks cv2.minEnclosingCircle  This helps to find position on screens'''
    def getInfo(self,info):
        ((x, y), radius) = info
        self.x = int(x)
        self.y = int(y)
        self.radius = int(radius)


