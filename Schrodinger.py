#!/usr/bin/env python
#coding:utf-8
from numpy import*
from Tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#----------------------------------------------------------------------
class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
  
    def createWidgets(self):
        self.WellNumber = Label(self)
        self.WellNumber["text"] = "Well Number"
        self.WellNumber.grid(row=1, column=0,ipadx=12,ipady=5)
        self.WellNumberField = Entry(self,justify='center')
        self.WellNumberField["width"] = 10
        self.WellNumberField.insert(0,2)
        self.WellNumberField.grid(row=1, column=1, columnspan=5)
        
        self.Wellwidth = Label(self)
        self.Wellwidth["text"] = "Well width (A)"
        self.Wellwidth.grid(row=2, column=0,ipadx=12,ipady=5)
        self.WellwidthField = Entry(self,justify='center')
        self.WellwidthField["width"] = 10
        self.WellwidthField.insert(0,5)
        self.WellwidthField.grid(row=2, column=1, columnspan=5)

        self.ElectronMass = Label(self)
        self.ElectronMass["text"] = "electron mass (m0)"
        self.ElectronMass.grid(row=3, column=0,ipadx=12,ipady=5)
        self.ElectronMassField = Entry(self,justify='center')
        self.ElectronMassField["width"] = 10
        self.ElectronMassField.insert(0,5)
        self.ElectronMassField.grid(row=3, column=1, columnspan=5)

        self.Windowwidth = Label(self)
        self.Windowwidth["text"] = "left/right window width (A)"
        self.Windowwidth.grid(row=1, column=10,ipadx=12,ipady=5)   
        self.WindowwidthField = Entry(self,justify='center')   
        self.WindowwidthField["width"] = 10
        self.WindowwidthField.insert(0,15)
        self.WindowwidthField.grid(row=1, column=11, columnspan=5)  
        
        self.Barrierwidth = Label(self)
        self.Barrierwidth["text"] = "barrier width (A)"
        self.Barrierwidth.grid(row=2, column=10,ipadx=12,ipady=5)   
        self.BarrierwidthField = Entry(self,justify='center')   
        self.BarrierwidthField["width"] = 10  
        self.BarrierwidthField.insert(0,2)
        self.BarrierwidthField.grid(row=2, column=11, columnspan=5)         
        
        self.BarrierPotential = Label(self)
        self.BarrierPotential["text"] = "barrier potential (eV)"
        self.BarrierPotential.grid(row=3, column=10,ipadx=12,ipady=5)   
        self.BarrierPotentialField = Entry(self,justify='center')   
        self.BarrierPotentialField["width"] = 10
        self.BarrierPotentialField.insert(0,2)
        self.BarrierPotentialField.grid(row=3, column=11, columnspan=5)
        
        self.Periodic = Label(self)
        self.Periodic["text"] = "Periodic"
        self.Periodic.grid(row=1, column=23,ipady=5,sticky=W)   
        self.PeriodicCheckbutton = Checkbutton(self)
        self.var=BooleanVar()
        self.PeriodicCheckbutton['variable']=self.var
        self.PeriodicCheckbutton.grid(row=1, column=20,ipady=5,sticky=E ) 
        
        self.Empty = Label(self)
        self.Empty["text"]="       "
        self.Empty.grid(row=2 ,column=18)
        self.CarrierDensity = Label(self)
        self.CarrierDensity["text"] = "Carrier density"
        self.CarrierDensity.grid(row=2, column=23,ipady=5)   
        self.CarrierDensityCheckbutton = Checkbutton(self)
        self.var2=BooleanVar()
        self.CarrierDensityCheckbutton['variable']=self.var2
        self.CarrierDensityCheckbutton.grid(row=2, column=20,ipady=5,sticky=E )
        
        self.Efn = Label(self)
        self.Efn["text"] = "Efn"
        self.Efn.grid(row=3, column=20,ipadx=12,ipady=5)
        self.EfnField = Entry(self,justify='center')
        self.EfnField["width"] = 5
        self.EfnField.insert(0,0.0)
        self.EfnField.grid(row=3, column=22, columnspan=5)

        self.Calculate = Button(self)
        self.Calculate["text"] = "calculate"
        self.Calculate["command"] = self.draww
        self.Calculate.grid(row=1, column=30)
        
        self.EigenValueNumber = Label(self)
        self.EigenValueNumber["text"] = "Eigen Value Number"
        self.EigenValueNumber.grid(row=2, column=30,ipadx=12,ipady=2,sticky=S)
        self.EigenValueNumberField = Entry(self,justify='center')   
        self.EigenValueNumberField["width"] = 10
        self.EigenValueNumberField.grid(row=3, column=30, columnspan=5)        

        self.EigenValue = Label(self)
        self.EigenValue["text"] = "EigenValue"
        self.EigenValue.grid(row=1, column=40,ipadx=12,ipady=5)

        self.EigenValueList = Listbox(self)
        self.EigenValueList["height"] = 5
        self.EigenValueList["selectmode"] = BROWSE
        self.EVLscrollbar = Scrollbar(self)
        self.EigenValueList.configure(yscrollcommand = self.EVLscrollbar.set)
        self.EVLscrollbar.grid(row=2, column=41,rowspan=2,sticky=N+S+W)
        self.EVLscrollbar['command'] = self.EigenValueList.yview
        self.EigenValueList.grid(row=2, column=40, rowspan=2)      
        
        self.EigenValueList.delete(0,END)
        g,h,j,z,o=self.CEigen()
        for i in range(g.shape[0]):   
            self.EigenValueList.insert(END,g[i])
        self.EigenValueList["width"] = 10  

    
    def draww(self):
        drawPic()
        drawPic2()         
        g,h,j,z,o=self.CEigen()        
        yy=0
        self.EigenValueNumberField.delete(0,END)
        try:
            yy=int(self.EigenValueList.curselection()[0])
            self.EigenValueNumberField.insert(0,yy+1)
        except:
            self.EigenValueNumberField.insert(0,1)
        self.EigenValueList.delete(0,END)            
        for i in range(g.shape[0]):   
            self.EigenValueList.insert(END,g[i])
        self.EigenValueList["width"] = 10
        self.EigenValueList.select_set(yy)

        
    def CEigen(self):
        VOO=float(self.BarrierPotentialField.get())
        wellW=float(self.WellwidthField.get())
        barrierW=float(self.BarrierwidthField.get())
        windowW=float(self.WindowwidthField.get())
        NW=float(self.WellNumberField.get())
        mkk=float(self.ElectronMassField.get())
        efn=float(self.EfnField.get())
                
        Lunit=(wellW*10**-10)/50
        totalL=(NW*wellW+(NW-1)*barrierW+2*windowW)*(10**-10)
        N=totalL/Lunit+1

        hbar=1.05*10**-34
        mO=9.11*10**-31
        meff=mkk*mO
        eO=1.6*10**-19
        VO=VOO*eO
        kB=1.38*10**-23
        T=300.0
        
        
        dx=Lunit
        x=arange(0,totalL,totalL/N)*10**10
        WL=array([windowW*10**-10])
        WR=array([(windowW+wellW)*10**-10])
        WLP=array([WL[0]/dx])
        WRP=array([WR[0]/dx])
        for i in range(1,int(NW)):
            WL=append(WL,WL[i-1]+(wellW+barrierW)*10**-10)
            WR=append(WR,WR[i-1]+(wellW+barrierW)*10**-10)
        for i in range(1,int(NW)):
            WLP=append(WLP,WL[i]/dx)
            WRP=append(WRP,WR[i]/dx)
        Ham=zeros([x.shape[0],x.shape[0]])
        const=-hbar**2/2/meff/dx**2
        Ham[0,0]=-2
        Ham[0,1]=1
        for i in range(1,x.shape[0]-1):
            Ham[i,i]=-2
            Ham[i,i-1]=1
            Ham[i,i+1]=1
        Ham[x.shape[0]-1,x.shape[0]-1]=-2
        Ham[x.shape[0]-1,x.shape[0]-2]=1
            
        VVV=array([VO])
        for i in range(1,x.shape[0]):
            VVV=append(VVV,VO)
        for j in range(int(NW)):
            for i in range(int(WLP[j]),int(WRP[j])):
                VVV[i]=VVV[i]-VO
        Ham=Ham*const
        for i in range(int(N)):
            Ham[i,i]=Ham[i,i]+VVV[i]
        Ham=Ham/eO
        Eigenvalue,Evector=linalg.eigh(Ham)

        phisquare=zeros([x.shape[0],x.shape[0]])
        phi=zeros([x.shape[0],x.shape[0]])
        n2d=zeros([x.shape[0]])
        n3d=zeros([x.shape[0],x.shape[0]])
        for i in range(int(N)):
            phisquare[:,i]=abs(Evector[:,i])**2
            sumtotal=sum(phisquare[:,i])*dx
            phi[:,i]=Evector[:,i]/sqrt(sumtotal)
            n2d[i]= meff/pi/hbar**2*kB*T*log(1+exp((efn-Eigenvalue[i])*eO/kB/T))/10**-8
            n3d[:,i]=n2d[i]*phisquare[:,i]

        return Eigenvalue,Evector,VVV/eO,x,n3d       
        
#----------------------------------------------------------------------        

def drawPic2():
 
    g,h,j,z,o=app.CEigen()

    drawPic2.f.clf()
    drawPic2.a=drawPic2.f.add_subplot(111)
      
    y2=j 

    try:
        bb=h[:,app.EigenValueList.curselection()[0]]
    except:
        bb=h[:,0]
    scalla=max(abs(bb))
    bbscale=bb/scalla
    if app.var.get() == True:
        bbscale=bbscale*-1
    try:
        Epos=g[int(app.EigenValueList.curselection()[0])]
    except:
        Epos=g[0]
    Refpos=real(bbscale[1])
    movepos=Epos-Refpos    

    y1=real(bbscale)+movepos           
    drawPic2.a.plot(z,y1,color='b')
    drawPic2.a.plot(z,y2,color='r')   
    drawPic2.a.set_ylabel('potential V (eV)')
    drawPic2.a.set_title('x (A)')
    drawPic2.canvas.show()
    drawPic2.canvas.get_tk_widget().grid(row=24, columnspan=4)              
    

def drawPic():
        
    g,h,j,z,o=app.CEigen()
    drawPic.f.clf()
    drawPic.a=drawPic.f.add_subplot(111)
    if app.var2.get() == True:
        try:
            bb=o[:,app.EigenValueList.curselection()[0]]
        except:
            bb=o[:,0]
        x=z
        y=real(bb)
        if app.var.get() == True:
            y*=-1        

        drawPic.a.set_ylabel('carrier density (1/cm^3)')
        drawPic.a.plot(x,y)    
        drawPic.canvas.show()
        drawPic.canvas.get_tk_widget().grid(row=10, columnspan=4)
        
    else:
        try:
            bb=h[:,app.EigenValueList.curselection()[0]]
        except:
            bb=h[:,0]
        x=z
        y=real(bb)
        if app.var.get() == True:
            y*=-1        

        drawPic.a.set_ylabel('Psi(x)')
        drawPic.a.plot(x,y)    
        drawPic.canvas.show()
        drawPic.canvas.get_tk_widget().grid(row=10, columnspan=4)

if __name__ == '__main__':

    root = Tk()  
    app = GUIDemo(master=root)
    app.master.title("1D Schrodinger")
    matplotlib.use('Agg')
    
    drawPic.f = Figure(figsize=(10,3), dpi=100) 
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=10, columnspan=4)

    drawPic2.f = Figure(figsize=(10,3), dpi=100) 
    drawPic2.canvas = FigureCanvasTkAgg(drawPic2.f, master=root)
    drawPic2.canvas.show()
    drawPic2.canvas.get_tk_widget().grid(row=24, columnspan=4)    
app.mainloop()  
