import tkinter as tk
from tkinter import messagebox

# ข้อมูลสมาชิกกลุ่มหมวกฟางทั้ง 10 คน
CHARACTERS = [
    {"name": "มังกี้ ดี ลูฟี่", "is_male": True, "is_founder": True, "has_fruit": True, "job": "กัปตัน", "hair": "ดำ"},
    {"name": "โรโรโนอา โซโร", "is_male": True, "is_founder": True, "has_fruit": False, "job": "นักดาบ", "hair": "เขียว"},
    {"name": "นามิ", "is_male": False, "is_founder": True, "has_fruit": False, "job": "ต้นหน", "hair": "ส้ม"},
    {"name": "อุซป", "is_male": True, "is_founder": True, "has_fruit": False, "job": "พลแม่นปืน", "hair": "ดำ"},
    {"name": "ซันจิ", "is_male": True, "is_founder": False, "has_fruit": False, "job": "กุ๊ก", "hair": "เหลือง"},
    {"name": "โทนี่ โทนี่ ช็อปเปอร์", "is_male": True, "is_founder": False, "has_fruit": True, "job": "หมอ", "hair": "น้ำตาล"},
    {"name": "นิโค โรบิน", "is_male": False, "is_founder": False, "has_fruit": True, "job": "นักโบราณคดี", "hair": "ดำ"},
    {"name": "แฟรงกี้", "is_male": True, "is_founder": False, "has_fruit": False, "job": "ช่างซ่อมเรือ", "hair": "ฟ้า"},
    {"name": "บรู๊ค", "is_male": True, "is_founder": False, "has_fruit": True, "job": "นักดนตรี", "hair": "ดำ"},
    {"name": "จินเบ", "is_male": True, "is_founder": False, "has_fruit": False, "job": "คนคุมหางเสือ", "hair": "ดำ"}
]

# คำถามที่ใช้แยกแยะ
QUESTIONS = [
    ("ตัวละครนี้เป็น 'ผู้ชาย' ใช่ไหม?", "is_male"),
    ("ตัวละครนี้เป็นสมาชิก 5 คนแรก (รวมลูฟี่) ที่เข้ากลุ่มใช่ไหม?", "is_founder"),
    ("ตัวละครนี้มีพลังของ 'ผลปีศาจ' ใช่ไหม?", "has_fruit"),
    ("ตัวละครนี้มีผม 'สีดำ' ใช่ไหม?", "hair", "ดำ"),
]

class StrawHatGuesser:
    def __init__(self, root):
        self.root = root
        self.root.title("Straw Hat Crew Guesser")
        self.root.geometry("400x350")
        self.root.configure(bg="#FFF5E1") # เรือโจรสลัด แบบวันพีซ

        self.current_list = CHARACTERS.copy()
        self.q_index = 0

        self.label = tk.Label(root, text="มาทายตัวละครในกลุ่มหมวกฟางกับน้องชุ้นกัน", 
                              font=("Arial", 11, "bold"), bg="#FFF5E1", wraplength=350)
        self.label.pack(pady=20)

        self.q_text = tk.Label(root, text="", font=("Arial", 13), bg="#FFF5E1", fg="#8B4513")
        self.q_text.pack(pady=30)

        self.btn_frame = tk.Frame(root, bg="#FFF5E1")
        self.btn_frame.pack(pady=20)

        tk.Button(self.btn_frame, text="ใช่", width=12, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: self.process(True)).grid(row=0, column=0, padx=10)
        tk.Button(self.btn_frame, text="ไม่ใช่", width=12, bg="#F44336", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: self.process(False)).grid(row=0, column=1, padx=10)

        self.ask()

    def ask(self):
        if self.q_index < len(QUESTIONS) and len(self.current_list) > 1:
            self.q_text.config(text=QUESTIONS[self.q_index][0])
        else:
            self.show_result()

    def process(self, answer):
        q_data = QUESTIONS[self.q_index]
        key = q_data[1]
        
        if len(q_data) == 3: # กรณีเช็คสีผม
            val = q_data[2]
            self.current_list = [c for c in self.current_list if (c[key] == val) == answer]
        else: # กรณี True/False
            self.current_list = [c for c in self.current_list if c[key] == answer]

        self.q_index += 1
        self.ask()

    def show_result(self):
        if len(self.current_list) >= 1:
            # ถ้าเหลือมากกว่า 1 ให้เลือกคนแรกที่ตรงเงื่อนไขที่สุด
            char = self.current_list[0]
            msg = f"ตัวละครที่คุณคิดคือ...\n\n🏴‍☠️ {char['name']} 🏴‍☠️\nตำแหน่ง: {char['job']}"
        else:
            msg = "หาไม่เจอเลย! คุณแอบนึกถึงแครอทหรือวีวี่หรือเปล่าครับ?"
        
        messagebox.showinfo("จับได้แล้ว!", msg)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StrawHatGuesser(root)
    root.mainloop()
