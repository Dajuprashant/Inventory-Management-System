from tkinter import Tk, Label, Entry, Button, StringVar

def whenPurchaseItem():
    purchase=Tk()
    purchase.config(bg="#545454")
    purchase.title("Purchase Item")
    purchase.geometry("600x300")
    purchase.minsize(height=300,width=600)
    purchase.maxsize(height=300,width=600)
    
    # Purchase Label title
    title=Label(purchase,text="Purchase Item",font=("Arial",23),bg="#545454",fg="white").pack(pady=(15,0))
    
    # for text field labels
    product_name_label=Label(purchase,text="Product Name",bg="#545454",fg="white",font=("Arial",10)).place(x=70,y=95)
    quantity_label = Label(purchase,text="Quantity",bg="#545454",fg="white",font=("Arial",10)).place(x=320,y=95)
    costprice_label = Label(purchase,text="Cost Price",bg="#545454",fg="white",font=("Arial",10)).place(x=427,y=95)
    
    # for text fields
    product_name_field=Entry(purchase,width=40)
    product_name_field.place(x=60,y=120,height=30)
    
    quantity_var = StringVar(value='')  # Set initial value to '0'
    quantity_field=Entry(purchase,width=15, textvariable=quantity_var)
    quantity_field.place(x=320,y=120,height=30)
    
    costprice_var = StringVar(value='')  # Set initial value to '0'
    costprice_field=Entry(purchase,width=18, textvariable=costprice_var)
    costprice_field.place(x=430,y=120,height=30)
    
    # for confirm button
    confirm_button=Button(purchase, text="Confirm Purchase", height=2, width=22, border=0, bg="#004789", fg="white",font=("Arial",10,"bold"))
    confirm_button.place(x=210,y=230)
    
    # for total label
    total_purchase = Label(purchase,font=("Arial",16),bg="#545454",fg="white")
    total_purchase.place(x=450,y=234)

    def calculate_total(*args):
        try:
            totalPurchaseAmt = int(costprice_var.get()) * int(quantity_var.get())
            total_purchase.config(text=f"Total: {totalPurchaseAmt}")
        except ValueError:
            total_purchase.config(text="Invalid input")

    quantity_var.trace_add("write", calculate_total)
    costprice_var.trace_add("write", calculate_total)
    purchase.mainloop()

whenPurchaseItem()
