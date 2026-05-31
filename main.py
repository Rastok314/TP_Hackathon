import os

folder_path = "inbox"
keywords = ["partner"]

keywords = [k.lower() for k in keywords]
print("ВСЕ файлы:", os.listdir(folder_path))
found = False

for filename in os.listdir(folder_path):
    print("Проверяю файл:", filename)

    if filename.endswith(".txt") or filename.endswith(".log"):
        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()

                for word in keywords:
                    if word in content:
                        print("✔ найдено:", word, "в", filename)
                        found = True

        except Exception as e:
            print("Ошибка:", e)

if not found:
    print("\nНичего не найдено")