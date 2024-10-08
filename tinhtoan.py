import tkinter as tk
from tkinter import ttk
from tkinter import Menu, messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x400")
        

        # Menu
        self.create_menu()

        # Tabs
        self.create_tabs()

        # Danh sách lịch sử tính toán
        self.history = []

    def create_menu(self):
        # Tạo menu chính
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # Tạo menu File
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Tạo menu Help
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def create_tabs(self):
        # Tạo notebook (tab container)
        tab_control = ttk.Notebook(self.root)

        # Tab 1: Basic calculator
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Calculator')
        self.create_calculator(tab1)

        # Tab 2: Lịch sử tính toán
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Lịch sử tính toán')
        self.create_history_tab(tab2)

        tab_control.pack(expand=1, fill="both")

    def create_calculator(self, frame):
        

        # Tạo các label và entry cho số thứ nhất, số thứ hai, và phép tính
        label1 = tk.Label(frame, text="Số thứ nhất:", font=('Arial', 12), bg='#f0f4f7')
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.num1_entry = tk.Entry(frame, width=15, font=('Arial', 12), bg='#ffffff')
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        label2 = tk.Label(frame, text="Số thứ hai:", font=('Arial', 12), bg='#f0f4f7')
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.num2_entry = tk.Entry(frame, width=15, font=('Arial', 12), bg='#ffffff')
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        label3 = tk.Label(frame, text="Phép tính:", font=('Arial', 12), bg='#f0f4f7')
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Tạo OptionMenu cho phép tính
        self.operation_var = tk.StringVar(value="+")  # Giá trị mặc định là "+"
        operations = ["+", "-", "*", "/"]
        self.operation_menu = tk.OptionMenu(frame, self.operation_var, *operations)
        self.operation_menu.config(bg='#ffffff', font=('Arial', 12))
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)

        # Nút tính toán
        calc_button = tk.Button(frame, text="Tính toán", command=self.calculate, font=('Arial', 12), bg='#4CAF50', fg='white')
        calc_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Hiển thị kết quả
        self.result_label = tk.Label(frame, text="Kết quả: ", font=('Arial', 12), bg='#f0f4f7')
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def create_history_tab(self, frame):
        

        # Tạo Label cho lịch sử
        history_label = tk.Label(frame, text="Lịch sử tính toán", font=('Arial', 14), bg='#f0f4f7')
        history_label.pack(pady=10)

        # Tạo Listbox để hiển thị lịch sử tính toán
        self.history_listbox = tk.Listbox(frame, height=10, width=50, font=('Arial', 12), bg='#ffffff')
        self.history_listbox.pack(pady=10)

        # Nút để xóa lịch sử
        clear_history_button = tk.Button(frame, text="Xóa lịch sử", command=self.clear_history, font=('Arial', 12), bg='#f44336', fg='white')
        clear_history_button.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                raise ValueError("Phép toán không hợp lệ!")

            self.result_label.config(text=f"Kết quả: {result}")

            # Thêm kết quả vào lịch sử
            self.history.append(f"{num1} {operation} {num2} = {result}")
            self.update_history()

        except ValueError as ve:
            messagebox.showerror("Error", f"Lỗi nhập liệu: {ve}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Không thể chia cho 0!")

    def update_history(self):
        # Cập nhật lịch sử tính toán trong Listbox
        self.history_listbox.delete(0, tk.END)
        for entry in self.history:
            self.history_listbox.insert(tk.END, entry)

    def clear_history(self):
        # Xóa lịch sử tính toán
        self.history.clear()
        self.update_history()

    def new_file(self):
        # Xóa các ô nhập và nhãn kết quả
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.operation_var.set("+")  # Đặt lại phép tính mặc định là "+"
        self.result_label.config(text="Kết quả: ")

    def about(self):
        messagebox.showinfo("About", "Trần Lê Kha - 2274802010359.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
