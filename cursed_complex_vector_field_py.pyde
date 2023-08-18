tScale = 0.001
scaler=0.05
su=1
sw=-3
class complexNum:
    def __init__(self,a,b):
        self.value = PVector(a,b)
    def sum(self,b):
        return complexNum(self.value.x+b.value.x,self.value.y+b.value.y)
    def sMult(self,s):
        return complexNum(self.value.x*s,self.value.y*s)
    def cMult(self,b):
        return complexNum(self.value.x*b.value.x-self.value.y*b.value.y,self.value.x*b.value.y+self.value.y*b.value.x)
def vecToCNum(a):
    return complexNum(a.x,a.y)
def cExp(z):
    return vecToCNum(exp(z.value.x)*PVector(cos(z.value.y),sin(z.value.y)))
def arg(z):
    return atan2(z.value.y,z.value.x)
def ln(z):
    return complexNum(log(z.value.mag()),arg(z))
def inv(z):
    return complexNum(cExp(ln(z)).sMult(-1).value.x,cExp(ln(z)).sMult(-1).value.y)
def functionFixer(f):
    return lambda z:f(z).value
def noZero(a):
    return (min(0.00001,a))
def setup():
    size(1000,1000)
    colorMode(HSB)
    noStroke()
def f(z):
    return inv(cExp(ln(z).sMult(5)).sum(z).sum(complexNum(1,0)))
class Arrow:
    def __init__(self,y1,x1,y2,x2,w):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = w
    def draw(self):
        x=self.x2-self.x1
        y=self.y2-self.y1
        theta = atan2(y,x)
        r=sqrt(x**2+y**2)
        pushMatrix()
        translate(self.y1,self.x1)
        rotate(-theta)
        line(-self.w/2,0,-self.w/2,r)
        line(-self.w/2,0,self.w/2,0)
        line(self.w/2,0,self.w/2,r)
        translate(0,r)
        line(-3*self.w/4,0,0,self.w)
        line(-self.w/2,0,-3*self.w/4,0)
        line(self.w/2,0,3*self.w/4,0)
        line(3*self.w/4,0,0,self.w)
        popMatrix()
class VectorField:
    def __init__(self,f):
        self.f=f
    def draw(self):
        for j in range(-width//2,width//2,int(1/scaler)):
            for i in range(-height//2,height//2,int(1/scaler)):
                result = self.f(complexNum(i*scaler,j*scaler));
                stroke(result.mag()*5+40,255,255);
                #result = PVector(1,0)
                #print(self.f(1,2))
                pushMatrix()
                translate(width//2,height//2)
                arrow = Arrow(i,j,i+1/(2*scaler)*self.f(complexNum(i*scaler,j*scaler)).x/(0.001+result.mag()),j+1/(2*scaler)*self.f(complexNum(i*scaler,j*scaler)).y/(0.001+result.mag()),int(5))
                arrow.draw()
                #line          (i,j,i+1/(2*scaler)*self.f(i*scaler,j*scaler).x/(0.1+result.mag()),j+1/(2*scaler)*self.f(i*scaler,j*scaler).y/(0.1+result.mag()))
                popMatrix()
class VectorFieldPoint:
    def __init__(self,vf,x,y):
        self.vf = vf
        self.x = x
        self.y = y
    def draw(self):
        global tScale
        x = [self.x]
        y = [self.y]
        global scaler
        s=int(1/(2*scaler))
        pushMatrix()
        translate(width//2,height//2)
        point(s*self.x,s*self.y)
        print(self.vf(self.x,self.y))
        for i in range(int(1/tScale)*50):
            x.append(x[len(x)-1]+self.vf(x[len(x)-1],y[len(y)-1]).x*tScale)
            y.append(y[len(y)-1]+self.vf(x[len(y)-1],y[len(y)-1]).y*tScale)
        for i in range(len(x)-1):
            stroke(0,255,255)
            line(s*x[i],s*y[i],s*x[i+1],s*y[i+1])
            #print(x[i])
        popMatrix()
vectorField = VectorField(functionFixer(f)) 
vectorFieldPoint = VectorFieldPoint(f,20,5)
a=Arrow(0,0,100,200,5)
a= complexNum(1,2)
b=complexNum(1,2)
print(arg(a))
def draw():
    background(0,0,0)
    vectorField.draw()
    stroke(255,255,255)
    strokeWeight(4)
    #vectorFieldPoint.draw()
    strokeWeight(1)
    
