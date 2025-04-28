import os
from PIL import Image

# Путь к корневой папке
root_folder = "img"  # Указываем папку img в текущей директории

# Поддерживаемые форматы изображений
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif")

# Функция для оптимизации изображения
def optimize_image(file_path):
    try:
        # Открываем изображение
        with Image.open(file_path) as img:
            # Если изображение в RGBA, конвертируем в RGB для форматов, не поддерживающих прозрачность
            if img.mode == "RGBA" and file_path.lower().endswith((".jpg", ".jpeg", ".bmp")):
                img = img.convert("RGB")
            
            # Оптимизация в зависимости от формата
            if file_path.lower().endswith((".jpg", ".jpeg")):
                img.save(file_path, "JPEG", quality=85, optimize=True)  # Сжатие JPEG
            elif file_path.lower().endswith(".png"):
                img.save(file_path, "PNG", optimize=True)  # Оптимизация PNG
            elif file_path.lower().endswith(".webp"):
                img.save(file_path, "WEBP", quality=80, method=6)  # Сжатие WebP
            elif file_path.lower().endswith(".bmp"):
                img.save(file_path, "BMP")  # BMP не имеет встроенной оптимизации, просто пересохраняем
            elif file_path.lower().endswith(".gif"):
                img.save(file_path, "GIF", optimize=True)  # Оптимизация GIF

        print(f"Оптимизировано: {file_path}")
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")

# Обход всех папок и подпапок
for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        # Проверяем, является ли файл изображением
        if filename.lower().endswith(VALID_EXTENSIONS):
            file_path = os.path.join(dirpath, filename)
            optimize_image(file_path)

print("Оптимизация завершена!")