import module1  # Імпортуємо модуль, для якого шукаємо файли .pyc
import os

module_path = os.path.dirname(module1.__file__)  # Отримуємо шлях до модуля
pycache_path = os.path.join(module_path, "__pycache__")  # Шлях до папки __pycache__
print(pycache_path)
