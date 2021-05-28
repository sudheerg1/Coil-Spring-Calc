from tkinter import *
from tkinter import ttk

#With Frames + Radiobutton-  Final

root = Tk()
root.title("Spring Calculator")


#Variables
material = StringVar()
material.set("spring steel")


#Frames

input_frame = LabelFrame(root, text = "Inputs (Mandatory)", padx=10, pady=10)
input_frame.pack(padx=10, pady=10)

constraint_frame = LabelFrame(root, text = "Constraints", padx=10, pady=10)
constraint_frame.pack(padx=10, pady=10)

filter_frame = LabelFrame(root, text = "Filters (Optional)", padx=10, pady=10)
filter_frame.pack(padx=10, pady=10)

output_frame = LabelFrame(root, text = "Results", padx=10, pady=10)
output_frame.pack(padx=10, pady=10)


"""Inputs"""

#Labels
Mat_Label = Label(input_frame, text = "Material:", padx=20, pady=20)
Li_Label = Label(input_frame, text= "Length Initial, Li: (in mm)")
Lf_Label = Label(input_frame, text= "Length Final, Lf: (in mm)")
Separator_Label = Label(input_frame, text="_"*120)

Mat_Label.grid(row=0, column=0)         
Li_Label.grid(row=2, column=0)
Lf_Label.grid(row=3, column=0)

#Entries
Radiobutton(input_frame, text="Spring Steel", variable=material, value="spring steel").grid(row=0, column=1)
Radiobutton(input_frame, text="SS 304", variable=material, value="ss304").grid(row=0, column=2)

Li_Entry = Entry(input_frame,width=25, borderwidth=5)
Li_Entry.grid(row=2, column=1, columnspan=2, padx=20, pady=10)

Lf_Entry = Entry(input_frame,width=25, borderwidth=5)
Lf_Entry.grid(row=3, column=1, columnspan=2, padx=20, pady=10)


"""Constraints"""
#Labels
fosLabel = Label(constraint_frame, text="\u2264  Factor of Safety, FOS  \u2264")
FiLabel = Label(constraint_frame, text="\u2264  Initial Force, Fi (in kgf)  \u2264")
FfLabel = Label(constraint_frame, text="\u2264  Final Force, Ff (in kgf)  \u2264")

fosLabel.grid(row=5, column=1)
FiLabel.grid(row=6, column=1)
FfLabel.grid(row=7, column=1)

#Entries
fosEntry1 = Entry(constraint_frame,width=10, borderwidth=5)
fosEntry1.grid(row=5, column=0, padx=10, pady=10)

fosEntry2 = Entry(constraint_frame,width=10, borderwidth=5)
fosEntry2.grid(row=5, column=4, padx=10, pady=10)

FiEntry1 = Entry(constraint_frame,width=10, borderwidth=5)
FiEntry1.grid(row=6, column=0, padx=10, pady=10)

FiEntry2 = Entry(constraint_frame,width=10, borderwidth=5)
FiEntry2.grid(row=6, column=4, padx=10, pady=10)

FfEntry1 = Entry(constraint_frame,width=10, borderwidth=5)
FfEntry1.grid(row=7, column=0, padx=10, pady=10)

FfEntry2 = Entry(constraint_frame,width=10, borderwidth=5)
FfEntry2.grid(row=7, column=4, padx=10, pady=10)


"""Filters"""
#Labels
wireDiaLabel = Label(filter_frame, text="\u2264  Wire Diameter, d (in mm)  \u2264")
CoilOD_Label = Label(filter_frame, text="\u2264  Coil Outer Diameter, OD (in mm)  \u2264")
Separator_Label3 = Label(filter_frame, text="_"*120)

wireDiaLabel.grid(row=9, column=1)
CoilOD_Label.grid(row=10, column=1)

#Entries
wireDiaEntry1 = Entry(filter_frame,width=10, borderwidth=5)
wireDiaEntry1.grid(row=9, column=0, padx=10, pady=10)

wireDiaEntry2 = Entry(filter_frame,width=10, borderwidth=5)
wireDiaEntry2.grid(row=9, column=4, padx=10, pady=10)

CoilOD_Entry1 = Entry(filter_frame,width=10, borderwidth=5)
CoilOD_Entry1.grid(row=10, column=0, padx=10, pady=10)

CoilOD_Entry2 = Entry(filter_frame,width=10, borderwidth=5)
CoilOD_Entry2.grid(row=10, column=4, padx=10, pady=10)

Li_Entry.insert(0, '29.5')
Lf_Entry.insert(0, '40.5')

fosEntry1.insert(0, '0.85')
fosEntry2.insert(0, '1.5')

FiEntry1.insert(0, '0.065')
FiEntry2.insert(0, '0.1')
FfEntry1.insert(0, '0.1')
FfEntry2.insert(0, '0.35')

wireDiaEntry1.insert(0, '0.3')
wireDiaEntry2.insert(0, '0.4')

CoilOD_Entry1.insert(0, '3')
CoilOD_Entry2.insert(0, '3.5')

def realCalc():
    
    top = Toplevel()
    top.title("Results")
    top.geometry("500x500")
    
    #Create Main Frame
    main_frame = Frame(top)
    main_frame.pack(fill=BOTH, expand=1)

    #Create Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #Add Scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    #Another Frame inside Canvas
    second_frame = Frame(my_canvas)

    #Add that New frame to a Window in the canvas
    my_canvas.create_window((0,0),window=second_frame, anchor="nw")   
    
    g = 9.80665
    pi = 3.141592653589793
    
    global material
    
    G = 79.3*1000 if material=="spring steel" else 73.0*1000 
    tau_all = 1020.0 if material=="spring steel" else 860.88
        
    li = float(Li_Entry.get())
    lf = float(Lf_Entry.get())  
    fos1 = float(fosEntry1.get())
    fos2 = float(fosEntry2.get())
    fi1  = float(FiEntry1.get())
    fi2  = float(FiEntry2.get())
    ff1  = float(FfEntry1.get())
    ff2  = float(FfEntry2.get())
    wd1 = float(wireDiaEntry1.get())
    wd2 = float(wireDiaEntry2.get())
    cd1 = float(CoilOD_Entry1.get())
    cd2 = float(CoilOD_Entry2.get())
    
    dx = lf - li
    Li1 = [li]
    x0 = [5,6,7,8,9] #Initial Extension
    d1 = [0.25, 0.3, 0.32,0.33,0.34,0.35, 0.4, 0.5] #Wire Dia
    OD1 = [2.5, 2.8, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5] #Coil Outer Dia
    p1 = [0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75, 0.76, 0.78, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5] #Pitch
    count = 0
    for Li in Li1:
        for d in d1:
            for OD in OD1:
                for p in p1:
                    for xo in x0:
                        D = OD - d
                        Ls = Li - 2*D - xo  #Body Length
                        n = Ls/p   #No. of Body Coils
                        k = (G*(d**4))/(8*n*(D**3))
                        Fi = k*xo/g  #Force Initial
                        Ff = k*(xo+dx)/g #Force Final in kgf

                        C = D/d 
                        K = (4*C-1)/(4*C-4)+0.615/C #Wahl's Factor
                        tau = (K*8*Ff*C*g)/(pi*d**2) #Shear Stress Max
                        fos = tau_all/tau #Factor of Safety

                        if (Fi>=fi1)and(Fi<fi2)and(Ff<=ff2):
                            if fos>=fos1 and d>=wd1:
                                if (p-d)>=0:
                                    count+=1
                                    if(count==50):
                                        return
                                    Label(second_frame, text="d,OD,p,xo,n: "+str(d)+" "+str(OD)+" "+str(p)+str(xo)+" "+str(round(n,1))).pack()
                                    Label(second_frame, text="Fi,Ff: "+str(round(Fi,3))+" "+str(round(Ff,3))).pack()
                                    Label(second_frame, text="f: "+str(round(fos,2))).pack()
                                    Label(second_frame, text="Body Length: "+str(round(Ls,3))).pack()
                                    Label(second_frame, text="C2C Length: "+str(round(Ls+OD,3))).pack()
                                    Label(second_frame, text="Length Inside plus x0: "+str(round(Li,3))).pack()
                                    Label(second_frame, text="*"*50).pack()

    
    
myButton = Button(root,text="Calculate",padx=150, pady=10, bg="#5DCE5D", fg="black", command = lambda: realCalc())
myButton.pack()

root.mainloop()
