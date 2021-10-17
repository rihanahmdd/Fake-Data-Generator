import tkinter as tk
from tkinter import ttk, messagebox
from faker import Faker
from faker import Factory
import os
from csv import DictReader, DictWriter



root = tk.Tk()
root.title('Faker')
root.geometry("400x200")
root.resizable(0,0)

# Frames 
ouput_frame = tk.Frame(root)
ouput_frame.grid(row=2, columnspan=3, pady=20)
main_btn_frame = tk.Frame(root)
main_btn_frame.grid(row=3, columnspan=3, pady=10)

# Labels 
fake_region = ttk.Label(root, text="Select Region")
fake_region.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

fake_type = ttk.Label(root, text="Select Type")
fake_type.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Combobx
fake_region_cmbx = ttk.Combobox(root, width=30, state='readonly')
fake_region_cmbx['values']=("American", "Indian", "Italian", "Japanese", 'Chinese')
fake_region_cmbx.set("Indian")
fake_region_cmbx.grid(row=0, column=1, padx=8)

fake_type_cmbx = ttk.Combobox(root, width=30, state='readonly')
fake_type_cmbx['values']=(
    'Name', 'Male Name', 'Female Name', 'First Name', 'Last Name', 'Time', 'Date', 'Date Time', 'Month', 'Year', 
    'Month Name', 'Day Of Week', 'Day Of Month', 'Time Zone', 'Century', 'Date Of Birth', 'Address',
    'Job', 'Phone Number', 'Email', 'Company Email', 'Url', 'Image Url', 'Hostname', 'Domain Name', 'Mac Address',
    'Words', 'Sentence', 'Text', 'Numbers', 'Currency', 'Profile',
    )

fake_type_cmbx.grid(row=1, column=1, padx=8)

# Entrybox 
output_entry = tk.Entry(ouput_frame, width=40, relief=tk.GROOVE)
output_entry.pack()

# Buttons 
copy_btn = ttk.Button(ouput_frame, text="Copy")
copy_btn.pack(pady=5)

setdflt_btn1 = ttk.Button(root, text="Set Default")
setdflt_btn1.grid(row=0, column=2, padx=5)

setdflt_btn2 = ttk.Button(root, text="Set Default")
setdflt_btn2.grid(row=1, column=2, padx=5)

exit_btn = ttk.Button(main_btn_frame, text="Exit")
exit_btn.grid(row=0, column=0, sticky=tk.E, padx=5)

generate_btn = ttk.Button(main_btn_frame, text="Generate")
generate_btn.grid(row=0, column=1, sticky=tk.E)

# Check Button
theme_var = tk.IntVar()
theme = tk.Checkbutton(root, text= "Dark Theme", relief=tk.FLAT, variable=theme_var)
theme.grid(row=3, column=0, padx=2)

########################### Funcationality #########################################
if os.path.exists('Fake.csv'):
    if os.stat('Fake.csv').st_size == 0:
        with open('Fake.csv', 'w', newline='') as datafile:
            writer = DictWriter(datafile, fieldnames=['Theme', 'Region', 'Type'])
            writer.writeheader()
            writer.writerow({'Theme':'0', 'Region':'American', 'Type':'Name'})
    else:
        with open('Fake.csv', 'r', newline='') as datafile:
            writer = DictReader(datafile, fieldnames=['Theme', 'Region', 'Type'])
            next(writer)
            for data in writer:
                region = data['Region']
                typp = data['Type']
            fake_region_cmbx.set(region)
            fake_type_cmbx.set(typp)
else:
    with open('Fake.csv', 'w', newline='') as datafile:
        writer = DictWriter(datafile, fieldnames=['Theme', 'Region', 'Type'])
        writer.writeheader()
        writer.writerow({'Theme':'0', 'Region':'American', 'Type':'Name'})
    with open('Fake.csv', 'r', newline='') as datafile:
        writer = DictReader(datafile, fieldnames=['Theme', 'Region', 'Type'])
        next(writer)
        for data in writer:
            region = data['Region']
            typp = data['Type']
        fake_region_cmbx.set(region)
        fake_type_cmbx.set(typp)


# Default func
def default_func(abc, dflt):
    var = abc.get()
    with open('Fake.csv', 'r') as theme_data:
        reader = DictReader(theme_data, fieldnames=['Theme', 'Region', 'Type'])
        data_list = []
        for i in reader:
            data_list.append(i)
        data_list[1][f"{dflt}"]=var
        with open ('Fake.csv', 'w', newline='') as data:
            writer = DictWriter(data, fieldnames=['Theme', 'Region', 'Type'])
            writer.writerows(data_list)
            messagebox.showinfo('Success', f'{var.title()} Has Been Successfully Set To Default')

# Color Changer 
def color_changer():
    with open('Fake.csv', 'r') as theme_data:
        reader = DictReader(theme_data, fieldnames=['Theme', 'Region', 'Type'])
        next(reader)
        for i in reader:
            theme_value = i['Theme']
        if theme_value==str(1):
            theme.select()
            root['bg']='black'
            ouput_frame.config(bg='black')
            main_btn_frame.config(bg='black')
            fake_region.config(background='black', foreground='white')
            fake_type.config(background='black', foreground='white')
            output_entry.config(background='light Gray', foreground='black')
            theme.config(bg='black', fg='gray')
        else:
            root['bg']='white'
            ouput_frame.config(bg='white')
            main_btn_frame.config(bg='white')
            fake_region.config(background='white', foreground='black')
            fake_type.config(background='white', foreground='black')
            output_entry.config(background='white', foreground='black')
            theme.config(bg='white', fg='black')

# Set Default1 Button 
def set_default1():
    default_func(fake_region_cmbx, "Region")

# Set Default2 Button 
def set_default2():
    default_func(fake_type_cmbx, "Type")

# copy Button 
def copy_Button():
    data = output_entry.get()
    if len(data)==0:
        messagebox.showerror("Empty", "Nothing in box")
    else:
        root.clipboard_clear()
        root.clipboard_append(data)
        copy_btn.config(text='Copied')

# Theme updater 
def theme_updater():
    theme_value = theme_var.get()
    with open('Fake.csv', 'r') as theme_data:
        reader = DictReader(theme_data, fieldnames=['Theme', 'Region', 'Type'])
        data_list = []
        for i in reader:
            data_list.append(i)
        data_list[1]['Theme']=theme_value
        with open ('Fake.csv', 'w', newline='') as data:
            writer = DictWriter(data, fieldnames=['Theme', 'Region', 'Type'])
            writer.writerows(data_list)
        color_changer()

# exit Button 
def Exit_Button():
    result= messagebox.askyesno('Exit', "Do You Want To Exit ??")
    if result== True:
        root.destroy()
    if result== False:
        pass

# Generate Button 
def generate():
    copy_btn.config(text="Copy")
    typp = fake_type_cmbx.get().lower().strip()
    region = fake_region_cmbx.get().strip()
    if 'American' in region:
        region_slice = 'en_US'
    if 'Indian' in region:
        region_slice = 'hi_IN'
    if 'Japanese' in region:
        region_slice = 'ja_JP'
    if 'Italian' in region:
        region_slice = 'it_IT'
    if 'Chinese' in region:
        region_slice = 'zh_CN'

    fake = Faker(region_slice)

    if " " in typp:
        typp = typp.replace(" ", "_")
    
    fake_data = {
        'name': fake.name(), 'male_name': fake.name_male(), 'female_name':fake.name_female(), 
        'first_name': fake.first_name(), 'last_name': fake.last_name(), 'time': fake.time(), 'date': fake.date(),
        'date_time': fake.date_time(), 'month': fake.month(), 'year': fake.year(), 'month_name': fake.month_name(),
        'day_of_week': fake.day_of_week(), 'day_of_month': fake.day_of_month(), 'time_zone': fake.timezone(),
        'century': fake.century(), 'date_of_birth': fake.date_of_birth(), 'address': fake.address(),
        'job': fake.job(), 'phone_number': fake.phone_number(), 'email': fake.email(),
        'company_email': fake.company_email(), 'url': fake.url(), 'image_url': fake.image_url(), 
        'hostname': fake.hostname(), 'domain_name': fake.domain_name(), 'mac_address': fake.mac_address(), 
        'words': fake.words(), 'sentence': fake.sentence(), 'text': fake.text(1000), 'numbers': fake.random_int(),
        'currency': fake.currency(), 'profile': fake.profile(),
        }

    output_data =  fake_data[f'{typp}']

    try:
        if typp == 'profile':
            a = 31
        else:
            a = len(output_data)
    except TypeError:
        a = len(str(output_data))
    
    if a > 30:
        output_entry.delete(0, tk.END)
        pop_up_GUI = tk.Tk()
        pop_up_GUI.title("Result")
        pop_up_GUI.geometry("720x370")
        pop_up_GUI.resizable(0, 0)

        # labels 
        pop_up_GUI_lbl = tk.Label(pop_up_GUI, text='Profile', font=("cambria", '15', 'bold'))
        pop_up_GUI_lbl.pack(pady=5)
        
        # Frames 
        text_editor_frame = tk.Frame(pop_up_GUI, highlightbackground='black', highlightthickness=0.5)
        text_editor_frame.pack()
        pop_up_GUI_frame = tk.Frame(pop_up_GUI)
        pop_up_GUI_frame.pack(pady=6)

        # Text Editor and Scroll bar
        text_editor = tk.Text(text_editor_frame, height='15', width='75', wrap='word', font=("cambria", 12))
        text_scrollbar = tk.Scrollbar(text_editor_frame)
        text_editor.config(yscrollcommand=text_scrollbar.set)
        text_scrollbar.config(command=text_editor.yview)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_editor.pack(side=tk.LEFT)
        
        # Buttons 
        ext_btn = ttk.Button(pop_up_GUI_frame, text="Exit", command=pop_up_GUI.destroy)
        ext_btn.grid(row=0, column=0, padx=5)
        cpy_btn = ttk.Button(pop_up_GUI_frame, text="Copy")
        cpy_btn.grid(row=0, column=1)

        with open('Fake.csv', 'r') as theme_data:
            reader = DictReader(theme_data, fieldnames=['Theme', 'Region', 'Type'])
            next(reader)
            for i in reader:
                theme_value = i['Theme']
            if theme_value==str(1):
                pop_up_GUI.config(bg='black')
                pop_up_GUI_lbl.config(bg='black', fg='white')
                pop_up_GUI_frame.config(bg='black')
                text_editor_frame.config(bg='black')
                text_editor.config(bg='black', fg='white', insertbackground='white')
            else:
                pop_up_GUI.config(bg='white')
                pop_up_GUI_lbl.config(bg='white', fg='black')
                pop_up_GUI_frame.config(bg='white')
                text_editor_frame.config(bg='white')
                text_editor.config(bg='white', fg='black', insertbackground='black')

        if typp == 'profile':
            arranged_data = {
                'Name': output_data['name'], 'Date Of Birth': output_data['birthdate'], 'Sex': output_data['sex'],
                'Blood Group': output_data['blood_group'], 'Residence': output_data['residence'], 
                'Address': output_data['address'], 'User Name': output_data['username'], 'Mail': output_data['mail'],
                'Website': output_data['website'][0], 'Job': output_data['job'], 'Company': output_data['company']
            }
            arranged_data = list(arranged_data.items())[-1::-1]
            arranged_data =  dict(arranged_data)
            for items in arranged_data.items():
                key, value = items
                try:
                    if '\n' in value:
                        value = value.replace("\n", ', ')
                except TypeError:
                    pass
                finally:
                    text_editor.insert(1.0, f" {key}:\t\t{value}\n")
        else:
            pop_up_GUI_lbl.config(text=typp.title())
            text_editor.insert(1.0, fake_data[f'{typp}'])

        # Popup Funcationality
        def copy_Button2():
            text = text_editor.get(1.0, tk.END)
            if len(text)==1:
                messagebox.showerror("Empty", "Please Write Something")
            else:
                cpy_btn.config(text='Copied')
                root.clipboard_clear()
                root.clipboard_append(text)
        cpy_btn.config(command=copy_Button2)

        pop_up_GUI.mainloop()
    else:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_data)

# Binding commands 
setdflt_btn1.config(command=set_default1)
setdflt_btn2.config(command=set_default2)
copy_btn.config(command=copy_Button)
theme.config(command=theme_updater)
exit_btn.config(command=Exit_Button)
generate_btn.config(command=generate)



color_changer()
root.mainloop()

# Created and Programmed By RIHAN AHMED
