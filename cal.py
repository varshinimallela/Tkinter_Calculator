import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(True, True)
entry = tk.Entry(root,font=("Arial", 20),bg="dark grey",fg="black",bd=10,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipadx=10)
def press(v):
    entry.insert(tk.END,v)
def clear():
    entry.delete(0,tk.END)
def cal():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
buttons=["7","8","9","/","4","5","6","*","1","2","3","-","+","="]
r=1
c=0
for b in buttons:
    cmd=cal if b == "=" else lambda x=b: press(x)
    btn=tk.Button(root,text=b,width=5,height=2,font=("Arial", 14),bg="orange" if b in "+-*/=" else "dark grey",fg="white",bd=0,command=cmd)
    btn.grid(row=r, column=c, padx=5, pady=5)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,
          text="C",
          command=clear,
          font=("Segoe UI",14),
          bg="Red",
          fg="White",
          bd=0,
          width=22,
          height=2
).grid(row=r,column=c,columnspan=4,padx=10,pady=12)
root.mainloop()
