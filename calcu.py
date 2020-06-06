
from tkinter import *

raiz=Tk()

raiz.title("CALCU_lml")
raiz.iconbitmap("jari.ico")

miFrame=Frame(raiz)

miFrame.pack()
miFrame.config(bg='gray30',width=240,height=360)


operacion = ""
memoriaSuma = 0
memoriaResta = 0
memoriaMulti = 1
memoriaDivi = 1
variable=''
i=0


#--------------------------PANTALLA-------------------------------

numeroPantalla=StringVar(value='0')

pantalla=Entry(miFrame,textvariable=numeroPantalla,fg="white",font=('Helvetica',13,'bold'),justify="right",bg='gray5')
pantalla.place(x=0,y=0,width=240,height=60)


#-------------------------PULSACIONES TECLADO---------------------

def numeroPulsado(num):
    global operacion
    global variable

    if operacion!='':
        numeroPantalla.set(num)
        if operacion=='suma':
            variable='s'
        elif operacion=='resta':
            variable='r'
        elif operacion=='multi':
            variable='m'

        elif operacion=='divi':
            variable='d'

        operacion=''
    else:
        if numeroPantalla.get()=='0' and num=='0':
            numeroPantalla.set(num)
        elif numeroPantalla.get().count('.')==1 and num=='.':
            numeroPantalla.set(numeroPantalla.get())

        elif numeroPantalla.get()=='0' and num=='.':
            numeroPantalla.set('0.')

        
        elif numeroPantalla.get()=='0'and num!='0':
            numeroPantalla.set(num)

        else:
            numeroPantalla.set(numeroPantalla.get()+num)


    
   

#------------------------BORRAR-----------------------------------

def borra():
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    global operacion
    global i
    
    numeroPantalla.set('0')
    memoriaSuma=0
    memoriaResta=0
    memoriaMulti=1
    memoriaDivi=1
    operacion=''
    i=0
    boton9['state']=NORMAL
    boton8['state']=NORMAL
    boton7['state']=NORMAL
    boton6['state']=NORMAL
    boton5['state']=NORMAL
    boton4['state']=NORMAL
    boton3['state']=NORMAL
    boton2['state']=NORMAL
    boton1['state']=NORMAL
    boton0['state']=NORMAL
    botonSuma['state']=NORMAL
    botonRest['state']=NORMAL
    botonMult['state']=NORMAL
    botonDiv['state']=NORMAL
    botonComa['state']=NORMAL
    botonIgual['state']=NORMAL

    
#----------------------------OPERACIONES--------------------------

def suma():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    operacion = "suma"

    if memoriaResta == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        memoriaSuma = memoriaSuma + float(numeroPantalla.get())
        
                
    else:
        if memoriaResta != 0:
            memoriaSuma = memoriaResta - float(numeroPantalla.get())
            
            memoriaResta = 0
        elif memoriaMulti != 1:
            memoriaSuma = memoriaMulti * float(numeroPantalla.get())
            
            memoriaMulti = 1
        else:
            try:
                memoriaSuma = memoriaDivi / float(numeroPantalla.get())
                memoriaDivi = 1
            except ZeroDivisionError:
                memoriaSuma='ERROR'

    if memoriaSuma=='ERROR':
        numeroPantalla.set('ERROR')
        boton9['state']=DISABLED
        boton8['state']=DISABLED
        boton7['state']=DISABLED
        boton6['state']=DISABLED
        boton5['state']=DISABLED
        boton4['state']=DISABLED
        boton3['state']=DISABLED
        boton2['state']=DISABLED
        boton1['state']=DISABLED
        boton0['state']=DISABLED
        botonSuma['state']=DISABLED
        botonRest['state']=DISABLED
        botonMult['state']=DISABLED
        botonDiv['state']=DISABLED
        botonComa['state']=DISABLED
        botonIgual['state']=DISABLED

    else:
        numeroPantalla.set(memoriaSuma)
            
    
def resta():
    global operacion
    global memoriaResta
    global memoriaSuma
    global memoriaMulti
    global memoriaDivi
    operacion = "resta"

    if memoriaSuma == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        if memoriaResta == 0:
            memoriaResta = float(numeroPantalla.get()) - memoriaResta
        else:
            memoriaResta = memoriaResta - float(numeroPantalla.get())

    else:
        if memoriaSuma != 0:
            memoriaResta = memoriaSuma + float(numeroPantalla.get())
           
            memoriaSuma = 0
        elif memoriaMulti != 1:
            memoriaResta = memoriaMulti * float(numeroPantalla.get())
            
            memoriaMulti = 1
        else:
            try:
                memoriaResta = memoriaDivi / float(numeroPantalla.get())
                memoriaDivi = 1
            except ZeroDivisionError:
                memoriaResta='ERROR'

    if memoriaResta=='ERROR':
        numeroPantalla.set('ERROR')
        boton9['state']=DISABLED
        boton8['state']=DISABLED
        boton7['state']=DISABLED
        boton6['state']=DISABLED
        boton5['state']=DISABLED
        boton4['state']=DISABLED
        boton3['state']=DISABLED
        boton2['state']=DISABLED
        boton1['state']=DISABLED
        boton0['state']=DISABLED
        botonSuma['state']=DISABLED
        botonRest['state']=DISABLED
        botonMult['state']=DISABLED
        botonDiv['state']=DISABLED
        botonComa['state']=DISABLED
        botonIgual['state']=DISABLED

    else:
        numeroPantalla.set(memoriaResta)
    
    

def multi():
    global operacion
    global memoriaMulti
    global memoriaSuma
    global memoriaResta
    global memoriaDivi
    operacion = "multi"
    
    if memoriaSuma == 0 and memoriaResta == 0 and memoriaDivi == 1:
        memoriaMulti = float(numeroPantalla.get()) * memoriaMulti
        
    else:
        if memoriaSuma != 0:
            memoriaMulti = memoriaSuma + float(numeroPantalla.get())
            
            memoriaSuma = 0
        elif memoriaResta != 0:
            memoriaMulti = memoriaResta - float(numeroPantalla.get())
            
            memoriaResta = 0
        else:
            try:
                memoriaMulti = memoriaDivi / float(numeroPantalla.get())
                memoriaDivi = 1
            except ZeroDivisionError:
                memoriaMulti='ERROR'
    if memoriaMulti=='ERROR':
        numeroPantalla.set('ERROR')
        boton9['state']=DISABLED
        boton8['state']=DISABLED
        boton7['state']=DISABLED
        boton6['state']=DISABLED
        boton5['state']=DISABLED
        boton4['state']=DISABLED
        boton3['state']=DISABLED
        boton2['state']=DISABLED
        boton1['state']=DISABLED
        boton0['state']=DISABLED
        botonSuma['state']=DISABLED
        botonRest['state']=DISABLED
        botonMult['state']=DISABLED
        botonDiv['state']=DISABLED
        botonComa['state']=DISABLED
        botonIgual['state']=DISABLED
    else:
        numeroPantalla.set(memoriaMulti)
def divi():
    global operacion
    global memoriaDivi
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global i
    operacion = "divi"

    if memoriaSuma == 0 and memoriaResta == 0 and memoriaMulti == 1:
        if i==0:
            memoriaDivi=float(numeroPantalla.get())/memoriaDivi
            i+=1

        else:
            try:
                memoriaDivi=memoriaDivi/float(numeroPantalla.get())
            except ZeroDivisionError:
                memoriaDivi='ERROR'

        
    else:
        if memoriaSuma != 0:
            memoriaDivi = memoriaSuma + float(numeroPantalla.get())
            
            memoriaSuma = 0
        elif memoriaResta != 0:
            memoriaDivi = memoriaResta - float(numeroPantalla.get())
            
            memoriaResta = 0
        else:
            memoriaDivi = memoriaMulti * float(numeroPantalla.get())
            
            memoriaMulti = 1
    if memoriaDivi=='ERROR':
        numeroPantalla.set('ERROR')
        boton9['state']=DISABLED
        boton8['state']=DISABLED
        boton7['state']=DISABLED
        boton6['state']=DISABLED
        boton5['state']=DISABLED
        boton4['state']=DISABLED
        boton3['state']=DISABLED
        boton2['state']=DISABLED
        boton1['state']=DISABLED
        boton0['state']=DISABLED
        botonSuma['state']=DISABLED
        botonRest['state']=DISABLED
        botonMult['state']=DISABLED
        botonDiv['state']=DISABLED
        botonComa['state']=DISABLED
        botonIgual['state']=DISABLED
    else:
        numeroPantalla.set(memoriaDivi)
    

def igual():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    global variable
    global i
    
    if variable=='s' :
        numeroPantalla.set(memoriaSuma + float(numeroPantalla.get()))
        memoriaSuma = 0
    elif variable=='r':
        numeroPantalla.set(memoriaResta - float(numeroPantalla.get()))
        memoriaResta = 0
    elif variable=='m':
        numeroPantalla.set(memoriaMulti * float(numeroPantalla.get()))
        memoriaMulti = 1
    elif variable=='d':
        try:
            numeroPantalla.set(memoriaDivi / float(numeroPantalla.get()))
            memoriaDivi = 1
        except ZeroDivisionError:
            numeroPantalla.set('ERROR')
            boton9['state']=DISABLED
            boton8['state']=DISABLED
            boton7['state']=DISABLED
            boton6['state']=DISABLED
            boton5['state']=DISABLED
            boton4['state']=DISABLED
            boton3['state']=DISABLED
            boton2['state']=DISABLED
            boton1['state']=DISABLED
            boton0['state']=DISABLED
            botonSuma['state']=DISABLED
            botonRest['state']=DISABLED
            botonMult['state']=DISABLED
            botonDiv['state']=DISABLED
            botonComa['state']=DISABLED
            botonIgual['state']=DISABLED

    
    operacion=''
    memoriaSuma=0
    memoriaResta=0
    memoriaMulti=1
    memoriaMulti=1
    i=0
    variable=''

#----------------------------FILA 1-------------------------------
botonBorra=Button(miFrame,text="C",fg="black",background="cornsilk3",font=('Helvetica',10,'bold'),command=lambda:borra())
botonBorra.place(x=0,y=60,width=120,height=60)
botonDiv=Button(miFrame,text="/",background="dark orange",fg="white",font=('Helvetica',12,'bold'),command=lambda:divi())
botonDiv.place(x=120,y=60,width=60,height=60)
botonMult=Button(miFrame,text="X",background="dark orange",fg="white",font=('Helvetica',12,'bold'),command=lambda:multi())
botonMult.place(x=180,y=60,width=60,height=60)



#--------------------------FILA 2---------------------------------
boton7=Button(miFrame,text="7",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("7"))
boton7.place(x=0,y=120,width=60,height=60)
boton8=Button(miFrame,text="8",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("8"))
boton8.place(x=60,y=120,width=60,height=60)
boton9=Button(miFrame,text="9",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("9"))
boton9.place(x=120,y=120,width=60,height=60)
botonSuma=Button(miFrame,text="+",background="dark orange",fg="white",font=('Helvetica',15,'bold'),command=lambda:suma())
botonSuma.place(x=180,y=120,width=60,height=60)




#---------------------------FILA 3-------------------------------
boton4=Button(miFrame,text="4",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("4"))
boton4.place(x=0,y=180,width=60,height=60)
boton5=Button(miFrame,text="5",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("5"))
boton5.place(x=60,y=180,width=60,height=60)
boton6=Button(miFrame,text="6",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("6"))
boton6.place(x=120,y=180,width=60,height=60)
botonRest=Button(miFrame,text="-",background="dark orange",fg="white",font=('Helvetica',15,'bold'),command=lambda:resta())
botonRest.place(x=180,y=180,width=60,height=60)



#---------------------------FILA 4---------------------------------
boton1=Button(miFrame,text="1",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("1"))
boton1.place(x=0,y=240,width=60,height=60)
boton2=Button(miFrame,text="2",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("2"))
boton2.place(x=60,y=240,width=60,height=60)
boton3=Button(miFrame,text="3",background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("3"))
boton3.place(x=120,y=240,width=60,height=60)
botonIgual=Button(miFrame,text="=",background="dark orange",fg="white",font=('Helvetica',15,'bold'),command=lambda:igual())
botonIgual.place(x=180,y=240,width=60,height=120)



#-----------------------------FILA 5-----------------------------------

boton0=Button(miFrame,text="0",width=5,height=5,background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("0"))
boton0.place(x=0,y=300,width=120,height=60)
botonComa=Button(miFrame,text=".",width=5,height=5,background="gray30",fg="black",font=('Helvetica',10,'bold'),command=lambda:numeroPulsado("."))
botonComa.place(x=120,y=300,width=60,height=60)


raiz.mainloop()

