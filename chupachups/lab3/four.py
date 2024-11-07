import os
from for4 import directory

# рахуєм
def count_files_by_extensions(directory, extensions):
    files = os.listdir(directory)
    return len([file for file in files if any(file.endswith(ext) for ext in extensions)])


# джпг то пнг
def rename_extension_jpg_to_png(directory):
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            base = os.path.splitext(file)[0]
            new_name = base + ".mp3"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))


# ренейм то Біг буква
def rename_files_to_capitalized(directory):
    for file in os.listdir(directory):
        old_file = os.path.join(directory, file)
        if os.path.isfile(old_file):
            new_file = os.path.join(directory, file.lower().capitalize())
            os.rename(old_file, new_file)


# видалення
def delete_files_by_extension(directory, extension):
    for file in os.listdir(directory):
        if file.endswith(extension):
            os.remove(os.path.join(directory, file))


def main():
    directory = r'C:\Users\oleks\Desktop\pythonLab\lab3'

    print("🤍 Початковий вміст каталогу 🤍")
    for file in os.listdir(directory):
        print(file)

    # рахунок файлів c та dll
    extensions = [".exe", ".jpg"]
    total_files = count_files_by_extensions(directory, extensions)
    print(f"🧮 Файлів з розширеннями {extensions}: {total_files}")

    # ренейм юз функцію
    rename_extension_jpg_to_png(directory)
    print("📝 Каталог після заміни розширення .txt на .mp3")
    for file in os.listdir(directory):
        print(file)

    # ренейм в букві функцію
    rename_files_to_capitalized(directory)
    print("✏️ Каталог після перейменування файлів в нижній регістр з першою великою літерою")
    for file in os.listdir(directory):
        print(file)

    # видлаення пнг функцією
    delete_files_by_extension(directory, ".mp3")
    print("🗑️ Каталог після видалення файлів з розширенням .mp3")
    for file in os.listdir(directory):
        print(file)


if __name__ == "__main__":
    main()
