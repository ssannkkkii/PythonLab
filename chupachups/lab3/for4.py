import os

directory = r'C:\Users\yurachupa\Desktop\pythonLab\lab3'

files = [
    "_file1.doc", "file2.pdf", "file222_.docx", "cmd.exe", "sys.dll",
    "FiLe7_5.txt", "foto1.jpg", "song1.mp3", "!!!song2.mp3", "video.avi",
    "file9.txt", "file_3_document.docx", "my_document!!!.ppt", "main.c",
    "lab3.py", "lookup.xml", "pic1.png", "pic2.bmp"
]

os.makedirs(directory, exist_ok=True)

for file_name in files:
    file_path = os.path.join(directory, file_name)

    with open(file_path, 'w') as file:
        pass

print("😎 Файли створено успішно в:", directory)
