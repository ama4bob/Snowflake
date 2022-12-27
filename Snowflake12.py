numpy as np;

sizemod=1
size(1080*sizemod, 1080*sizemod)
fill(0, 0, 0.6)
rect(0, 0, 1080*sizemod, 1080*sizemod)

font("NaN-Overlap Regular", 200*sizemod)
baselineShift(20*sizemod)
alphabet = "†‡※¤⁂#!&‽¡abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZø§žÄÅÜâåêîïôöõÿŌŦŮėŵ"

# †‡※¤⁂#!&‽¡¿abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZø§žÄÅÜâåêîïôöõÿŌŦŮėŵ

flakecount=[]
flakeletter=[]
flakemult=[]
flakesize=[]
flakeweight=[]
flakexval=[]
flakeyval=[]
fillR=[]
fillG=[]
fillB=[]
rotateval=[]
rotatemult=[]
weightval=[]
rotatemod=[]
xposmod=[]
fillmod=[]
weightmod=[]
globweightmod=[]
decaymod=[]
decaymult=[]
tailsize=[]

counter = 0
counterlimit = 300
changecounter = 0
taillimit = 300*sizemod
xposition = 840*sizemod
yposition1 = 240*sizemod
yposition2 = 540*sizemod
yposition3 = 840*sizemod

size = 200*sizemod
fillval = 1
distance = 2*sizemod
speed = 5
weightspeed = 2
tailspeed = 3

#snowflakes

def drawsnf3(x):
    with savedState():
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(120, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(120, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(120, center=(flakexval[x], flakeyval[x]))
        rotate(360, center=(flakexval[x], flakeyval[x]))
    
    
    
def drawsnf4(x):
    with savedState():
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-90, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-90, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-90, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-90, center=(flakexval[x], flakeyval[x]))
        rotate(360, center=(flakexval[x], flakeyval[x]))
    
def drawsnf5(x):
    with savedState():
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-72, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-72, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-72, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-72, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-72, center=(flakexval[x], flakeyval[x]))
        rotate(360, center=(flakexval[x], flakeyval[x]))

def drawsnf6(x):
    with savedState():
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        text(flakeletter[x], (flakexval[x],flakeyval[x]), align="center")
        rotate(-60, center=(flakexval[x], flakeyval[x]))
        rotate(360, center=(flakexval[x], flakeyval[x]))
        
        
# system  
        
def flakeblank():
    flakecount.append(counterlimit+1)
    flakeletter.append("")
    flakemult.append("")
    flakesize.append("")
    flakeweight.append("")
    rotateval.append(0)
    rotatemult.append(0)
    fillR.append(fillval)
    fillG.append(fillval)
    fillB.append(fillval)
    flakexval.append(0)
    flakeyval.append(0)
    weightval.append(0)
    rotatemod.append(0)
    xposmod.append(0)
    fillmod.append(0)
    weightmod.append(0)
    globweightmod.append(0)
    decaymod.append(0)
    decaymult.append(0)
    tailsize.append(0)

    
for i in range (0, 3):
    flakeblank()

def init(x):
    flakecount[x] = 0
    select = randint(0,91)
    flakeletter[x] = alphabet[select]
    flakemult[x] = randint(3, 6)
    flakesize[x] = size
    flakeweight[x] = 0
    weightval[x] = randint(60, 200)
    rotatemult[x] = randint(1, 10)
    fill(fillR[x], fillG[x], fillB[x])
    if i == 0:
        flakexval[x] = xposition
        flakeyval[x] = yposition1
    elif i == 1:
        flakexval[x] = xposition
        flakeyval[x] = yposition2
    elif i == 2:
        flakexval[x] = xposition
        flakeyval[x] = yposition3
    rotatemod[x] = 0
    xposmod[x] = 0
    fillmod[x] = 0
    weightmod[x] = "true"
    globweightmod[x] = "true"
    decaymod[x] = 0
    decaymult[x] = randint(8, 20)
    tailsize[x] = taillimit-1
        
def update(u):
    fillR[u] = fillval
    fillG[u] = fillval
    fillB[u] = fillval
    flakexval[u] = xposition
    
def checkweight(k):
    if flakeweight[k] > 199:
        weightmod[k] = "false"
        flakeweight[k] -= 1*tailspeed
    elif flakeweight[k] < 61:
        weightmod[k] = "true"
        flakeweight[k] += 1*tailspeed
    elif weightmod[k] == "true":
        flakeweight[k] += 1*tailspeed
    elif weightmod[k] == "false":
        flakeweight[k] -= 1*tailspeed

def globalweight(e):
    if weightval[e] > 199:
        globweightmod[e] = "false"
        weightval[e] -= 1*weightspeed 
    elif weightval[e] < 61:
        globweightmod[e] = "true"
        weightval[e] += 1*weightspeed
    elif globweightmod[e] == "true":
        weightval[e] += 1*weightspeed
    elif globweightmod[e] == "false":
        weightval[e] -= 1*weightspeed
        
    
        
for i in range (0, 3):
    init(i)
print(flakecount, flakeletter, flakemult, flakesize, flakeweight, flakexval, flakeyval, fillR, fillG, fillB, rotatemult, decaymult, tailsize)

def draw(a):
    if flakemult[a] == 3:
        drawsnf3(a)
    elif flakemult[a] == 4:
        drawsnf4(a)
    elif flakemult[a] == 5:
        drawsnf5(a)
    else:
        drawsnf6(a)
        
def change(c):
    init(c)
    tailsize[c] = randint(taillimit/2, taillimit)


for frames in range(0, counterlimit):
    fill(0.9, 0.9, 1)
    rect(0, 0, 1080*sizemod, 1080*sizemod)
    font("NaN-Overlap Regular", size)
    baselineShift(20*sizemod)
    strokeWidth(2*sizemod)
    stroke(0.5,0,0)
    for w in range(0, 3):
        flakeweight[w] = weightval[w]
    #print("font", weightval, flakeweight)
    
    for n in range(0, taillimit):
        for p in range (0, 3):
            if n <= tailsize[p]:
                fontVariations(wght=flakeweight[p])
                #print(counter, weightval[p], flakeweight[p])
                #checkweight(p)
                fill(fillR[p], fillG[p], fillB[p])
                stroke(fillR[p], fillG[p], fillB[p])
                temprotate = rotateval[p] + rotatemod[p] + decaymod[p]
                rotate(temprotate, center=(flakexval[p], flakeyval[p]))
                draw(p)
                rotateneg = temprotate*-1
                rotate(rotateneg, center=(flakexval[p], flakeyval[p]))
                flakexval[p] -= distance
                rotateval[p] += 6/rotatemult[p]
                decaymod[p] += (n+1)/decaymult[p]
                if n != tailsize[p]-1:
                    filldiv = 0.8/tailsize[p]
                    fillR[p] -= filldiv
                    fillG[p] -= filldiv
                    fillB[p] -= filldiv
                else:
                    strokeWidth(0)
                    filldiv = 1
                    fillR[p] = filldiv
                    fillG[p] = filldiv
                    fillB[p] = filldiv
       
        counter += 1
    for w in range(0, 3):
        rotateval[w] = 0
        flakexval[w] = 840*sizemod
        fillR[w] = 1
        fillG[w] = 1
        fillB[w] = 1
        rotatemod[w] += 0.1*speed 
        decaymod[w] = 0
        globalweight(w)
    
    if changecounter == 0:
        dice = randint(1, 10)
        if dice == 1:
            i = randint(0, 2)
            change(i)
            changecounter = 60
            print(counter, i, changecounter, "change", flakeletter)
    else:
        changecounter -= 1
        print(changecounter)
    
    countstr=str(frames)
    # savename="/Users/jackllewellyn/Downloads/snowflake/test/frame-"+countstr+".png"
    # saveImage(savename)
    
    if frames != counterlimit-1:
        newPage()
# saveImage("/Users/jackllewellyn/Downloads/snowflake/snowflake10b.gif")

    
        
    