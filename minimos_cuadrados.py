from tkinter import *
import  numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#data_x=np.array([1,2,3,4,5])
#data_y=np.array([6,7,8,9,10])
#raw_data={'eje_x':data_x,'eje_y':data_y}
#df3 = DataFrame(raw_data,columns=['eje_x','eje_y'])
#df3.head()
#print(df3.iloc[0]['eje_x'])

#---------------CONFIGURACION---------------------------
Main_window = Tk()
Main_window.title("Calculadora minimos")
Main_window.geometry("400x400")
#---------------VARIABLES-------------------------------
valor_x=StringVar(value="")
valor_y=StringVar(value="")
data_x=np.array()
data_y=np.array()
position_colum=0

#---------------FUNCIONES-------------------------------
###
def mostrar_pantalla(data_x,data_y):
    raw_data={'eje_x':data_x,'eje_y':data_y}
    df3 = DataFrame(raw_data,columns=['eje_x','eje_y'])
    df3.head()

    root= Tk() 
    root.title("grafico")
    figure3 = plt.Figure(figsize=(5,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['eje_x'],df3['eje_y'], color = 'g')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)
    #ax3.legend(['Stock_Index_Price']) 
    #ax3.set_xlabel('Interest Rate')
    #ax3.set_title('Interest Rate Vs. Stock Index Price')
    root.mainloop()
###
def minimos_cuadrados(data_x,data_y):
    global valor_A,valor_B,valor_C
    x_p=data_x.mean()
    y_p=data_y.mean()
    #primera columna
    x_xp=data_x-x_p
    #segunda columna
    x_xp2=np.power(x_xp,2.0)
    #tercera columna
    x_xp_y=np.zeros(data_x.size)
    for i in range(0,data_x.size):
        x_xp_y[i]=x_xp[i]*data_y[i]
    #calculo de A y B
    sum_x_xp2=np.sum(x_xp2)
    sum_x_xp_y=np.sum(x_xp_y)
    B=sum_x_xp_y/sum_x_xp2
    A=y_p-(B*x_p)
    #cuarta columna
    di_2=np.zeros(data_x.size)
    for i in range(0,data_x.size):
        di=data_y[i]-A-(B*data_x[i])
        di_2[i]=pow(di,2)
    #calcular C
    C=np.sum(di_2)
    C/=(data_x.size-2)
    return x_xp,x_xp2,x_xp_y,di_2,A,B,C;
###
def plot_column(window,array):
    global position_colum
    for i in range(0,array.size):
        valor=Label(window,borderwidth = 2,
                        width = 20,
                        relief="ridge",
                        text=round(array[i],14))
        valor.grid(row=i,column=position_colum)
    position_colum+=1
###
def plot_matrix():
    string_x=valor_x.get()
    string_y=valor_y.get()
    data_x=np.fromstring(string_x,dtype=float,sep=',')
    data_y=np.fromstring(string_y,dtype=float,sep=',')
    if(data_x.size!=data_y.size):
        return
    #minimos
    c_1,c_2,c_3,c_4,A,B,C=minimos_cuadrados(data_x,data_y)
    #Ventana matrices
    new_window=Tk()
    
    new_window.title("Matrices")
    new_window.geometry("1000x300")
    var=np.array([1.1,2.2,3.3,4.4,5.5])
    var1=np.array([1.1,2.2,3.3,4.4,5.5])
    plot_column(new_window,data_x)
    plot_column(new_window,data_y)
    plot_column(new_window,c_1)
    plot_column(new_window,c_2)
    plot_column(new_window,c_3)
    plot_column(new_window,c_4)
    valor_A=DoubleVar(value=A)
    valor_B=DoubleVar(value=B)
    valor_C=DoubleVar(value=C)
    Titulo3= Label(new_window,text=valor_A.get())
    Titulo4= Label(new_window,text=valor_B.get())
    Titulo5= Label(new_window,text="A: ")
    Titulo6= Label(new_window,text="B: ")
    Titulo5.grid(row=data_x.size+1,column=0)
    Titulo3.grid(row=data_x.size+1,column=1)
    Titulo6.grid(row=data_x.size+2,column=0)
    Titulo4.grid(row=data_x.size+2,column=1)
    #Grafico
    mostrar_pantalla(data_x,data_y)
    #
    new_window.mainloop()
#----------------UI-------------------------------------
Titulo1= Label(Main_window,text="Valores x")
Titulo2= Label(Main_window,text="Valores y")

input1=    Entry(Main_window,textvariable=valor_x)
input2=    Entry(Main_window,textvariable=valor_y)
btn_lista = Button(Main_window,text = "Calcular",command = plot_matrix)
#----------------ESTRUCTURA UI--------------------------
Titulo1.pack()
input1.pack(ipady=3)
Titulo2.pack()
input2.pack()
btn_lista.pack()
Main_window.mainloop()
