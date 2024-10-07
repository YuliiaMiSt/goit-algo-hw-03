import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    """
    Рекурсивно перебирає файли в директорії і копіює їх у нову директорію,
    сортує за розширенням.
    """
    try:
        # Перебираємо всі елементи в вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Якщо елемент — директорія, викликаємо функцію рекурсивно
            if os.path.isdir(item_path):
                copy_files(item_path, dest_dir)
            else:
                # Якщо елемент — файл, отримуємо його розширення
                file_extension = os.path.splitext(item)[1][1:]
                if not file_extension:
                    file_extension = 'no_extension'

                # Створюємо піддиректорію для цього типу файлів
                target_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(target_dir, exist_ok=True)

                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item_path, os.path.join(target_dir, item))
                print(f'Копіюється файл {item} до {target_dir}')

    except Exception as e:
        print(f'Помилка при копіюванні файлів: {e}')


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання і сортування файлів за розширенням.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    args = parser.parse_args()

    src_dir = args.src_dir
    dest_dir = args.dest_dir

    # Перевіряємо наявність вихідної директорії
    if not os.path.exists(src_dir):
        print(f'Директорія {src_dir} не існує.')
        return

    # Створюємо директорію призначення, якщо вона не існує
    os.makedirs(dest_dir, exist_ok=True)

    # Запускаємо рекурсивне копіювання
    copy_files(src_dir, dest_dir)
    print(f'Копіювання завершено. Файли сортуються у {dest_dir}')

if __name__ == '__main__':
    main()
