import os
from time import strftime
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

class fileoperations:    
    def choosefile(self):
        filepath = filedialog.askopenfilename(initialdir="/",title="Select File", filetypes=(("G-code Files","*.gcode"),("all files","*.*")))
        self.filename = os.path.basename(filepath)
        text1.insert(INSERT,self.filename)
        text1.config(state="disabled")
        messagebox.showinfo("Notification","Enter Output file name")

    def convertfile(self):
        self.textboxinput = text2.get("1.0","end-1c")
        file1=open(self.filename,"r")
        file2=open(self.textboxinput,"w")
        lines = file1.readlines()
        for line in lines[0:100]:
            if(line[0] == ';'):
                if("LAYER_COUNT" in line):
                    self.totlayercount = line[len("LAYER_COUNT")+2:].strip()
                elif("LAYER" in line):
                    self.layernum = line[len("LAYER")+2:].strip()
                elif(line[1:5] == 'TYPE'):
                    self.type = line[len("TYPE") + 2:].strip()
            elif('G0' in line):
                if('X' in line):
                    start = line.find('X')
                    end = line.find(' ',start)
                    valx = float(line[start+1:end])

                    start = line.find('Y')
                    end = line.find(' ',start)
                    valy = float(line[start+1:end])

                    valx = int((valx-125)*7760/12.5)
                    valy = int((valy-125)*7760/12.5)
                    file2.write("0 X = " + str(valx) + " Y = " + str(valy) + '\n')

            elif('G1' in line):
                if('X' in line):
                    start = line.find('X')
                    end = line.find(' ',start)
                    valx = float(line[start+1:end])

                    start = line.find('Y')
                    end = line.find(' ',start)
                    valy = float(line[start+1:end])

                    valx = int((valx-125)*7760/12.5)
                    valy = int((valy-125)*7760/12.5)
                    file2.write("1 X = " + str(valx) + " Y = " + str(valy) + '\n')

        file1.close()
        file2.close()
                    

if __name__ == "__main__":
    root = Tk()
    root.title("G-Code to STP")
    root.geometry("640x360")
    fop = fileoperations()
    lbl = Label(root, text = 'File Converter', font=('Times New Roman',15))
    lbl.pack(side=TOP,pady=10)
    b = Button(root,text = 'Select file for conversion', command = fop.choosefile)
    b.pack()
    text1 = Text(root,height=2,width=30)
    text1.config(state="normal")
    text1.pack()
    label2 = Label(root,text='Set Output File name',font=('Times New Roman',10))
    label2.pack()
    text2 = Text(root,height=2,width=30)
    text2.pack()
    b2 = Button(root,text = 'Convert File',command = fop.convertfile)
    b2.pack()
    root.mainloop()
