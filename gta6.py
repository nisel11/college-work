from rich.console import Console
import time
import random
import os

# Python is a high-level, general-purpose programming language. 
# Its design philosophy emphasizes code readability with the use of significant indentation.
# Python is dynamically type-checked and garbage-collected. 
# It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 
# It is often described as a "batteries included" language due to its comprehensive standard library.
# BUT python is gay because of "pip install numpy pandas matplotlib seaborn scipy scikit-learn tensorflow keras flask django requests beautifulsoup4 lxml pillow pyqt5 sqlalchemy pytest jupyterlab plotly sympy opencv-python opencv-contrib-python pillow pydantic fastapi pyyaml boto3 sqlalchemy alembic gunicorn celery pytest-django pytest-cov flake8 black isort pylint mypy coverage sphinx sphinx-rtd-theme sphinx-autodoc-typehints pre-commit"
class GTA6:
    # Just init, nothing special
    def __init__(self):
        self.console = Console()
        os_type = os.name

    # I don't like apt but apt moo is best command ever
    def ascii_art(self):
        art = r"""
                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~ 🐄
        """
        self.console.print(art)

    # Generate powerful massive
    def _generate_arrays(self, num_arrays=5, array_length=10):
        return [[random.randint(0, 100) for _ in range(array_length)] for _ in range(num_arrays)]

    # Better manual input, not [1, 2, 3] just 1 2 3
    def _input_array(self):
        while True:
            self.console.print("[bold cyan]Введіть числа через пробіл:[/bold cyan]")
            raw = input(">>> ")
            try:
                nums = list(map(int, raw.split()))
                if not nums:
                    raise ValueError("Пустой ввод")
                return [nums]
            except ValueError:
                self.console.print("[bold red]Некоректний ввід. Введіть лише цілі числа через пробіл.[/bold red]")

    def find_strongest(self, arrays: list[list[int]]) -> tuple[list[int], int]:
        sums = [sum(arr) for arr in arrays]
        best_idx = max(range(len(sums)), key=lambda i: sums[i])
        best_arr = arrays[best_idx]
        return best_arr, max(best_arr)

    # Powerfull and rich loading bar
    def rich_loading(self, text, result_label, result, delay=True):
        if delay:
            with self.console.status(text, spinner="dots", spinner_style="magenta"):
                time.sleep(2)
            self.console.print(f"[bold green]{result_label}[/bold green] {result}\n")
        else:
            self.console.print(f"[bold green]{result_label}[/bold green] {result}\n")

    # Select what you want do
    def select_input_mode(self):
        self.console.print("[bold yellow]Оберіть режим введення:[/bold yellow]")
        self.console.print("1. Випадкова генерація масивів")
        self.console.print("2. Ручне введення одного масиву")
        self.console.print("3. Калькулятор")
        self.console.print("4. Дії з файлом")
        self.console.print("5. Вийти (До тесту класу Student)")

        choice = input(">>> ").strip()
        if choice == '1':
            self.do_arrays(user_input = False)
            return True
        elif choice == '2':
            self.do_arrays(user_input = True)
            return True
        elif choice == '3':
            self.calculator()
            return True
        elif choice == '4':
            self.choice_file()
            return True
        elif choice == '5':
            return False
        else:
            self.console.print("[bold red]Невірний вибір. Спробуйте ще раз.[/bold red]")
            return self.select_input_mode()

    # Calculator, no more
    def calculator(self):
        self.console.print("[bold yellow]Введіть математичний вираз (exit щоб вийти): [/bold yellow] ")
        while True:
            try:
                не_придумав = input('>>> ').strip()
                if не_придумав == 'exit':
                    break
                elif не_придумав == '':
                    continue
                result = eval(не_придумав)
                print(result)
            except ZeroDivisionError:
                self.console.print("[bold red]Ти шо здурів?[/bold red]")
            except UnicodeDecodeError:
                self.console.print("[bold red]Слухай, тут щось не так, попробуй ще раз[/bold red]")
            except Exception as e:
                if str(e) == "unterminated string literal (detected at line 1) (<string>, line 1)":
                    self.console.print("[bold red]Шось тут не те ти пишиш[/bold red]")
                elif str(e) == "invalid syntax (<string>, line 1)":
                    self.console.print("[bold red]Помилка: Інвалід синтаксис, ділення через / а не :, якщо це не з діленням проблеми, то надіюсь ви їх якось самі там виправите[/bold red]")
                else:
                    self.console.print(f"[bold red]Помилка: {str(e)}[/bold red]")

    def choice_file(self):
        self.console.print("[bold yellow]Перенесіть файл сюди або натисніть Enter для створення рандомного файлу[/bold yellow]")
        file_path = input().strip().strip('"').strip("'")

        if not file_path:
            arrays = self._generate_arrays()
            flat = [num for sublist in arrays for num in sublist]
            file_path = "file.txt"
            with open(file_path, 'w') as f:
                f.write("Привіт, світ!\n")
                f.write(' '.join(map(str, flat)))
            self.file_autocreated = True
        else:
            if not os.path.exists(file_path):
                self.console.print("[bold yellow]Файл не знайдено, будь ласка, виберіть реальний файл[/bold yellow]")
                return

        self.console.print("[bold yellow]1. Вичислити суму чисел[/bold yellow]")
        self.console.print("[bold yellow]2. Вивести вміст[/bold yellow]")
        choice = input(">>> ").strip()

        if choice == '1':
            with open(file_path) as f:
                lines = f.readlines()
                if len(lines) > 1:
                    numbers = list(map(int, lines[1].split()))
                    self.delete_system32(file_path, numbers)
        elif choice == '2':
            self.delete_system32(file_path, None)

    def delete_system32(self, file: str, flat = None):
        if not flat:
            with open(file, 'r') as file:
                content = file.read()
                print(content)
        else:
            print(sum(flat))

    def do_arrays(self, user_input: bool):
        if not user_input:
            delay = True
            arrays = self._generate_arrays()
        else:
            delay = False
            arrays = self._input_array()

        best_arr, best_num = self.find_strongest(arrays)
        print()
        self.rich_loading("🏆 Пошук найпотужнішого масиву...", "🏆 НАЙПОТУЖНІШИЙ МАСИВ:", best_arr, delay=delay)
        self.rich_loading("👑 Пошук найпотужнішого числа...", "👑 НАЙПОТУЖНІШЕ ЧИСЛО:", best_num, delay=delay)

    # Start GTA VI
    def start(self):
        self.ascii_art()
        if not self.select_input_mode():
            return

        input("Натисніть Enter щоб піти далі, в складний путь, який іноді не є шляхом до успіху...")

        os.system('cls' if os.name == 'nt' else 'clear')

        time.sleep(1)
        self.console.print("Далі тут студент якийсь йде, який погано вчиться, надіюсь його не відрахують /n")
        time.sleep(1)
        print()

class Student:
    def __init__(self, name: str, age: int, course: int): # Типізація даних в python: 😱 :horror: 😱
        self.name = name
        self.age = age
        self.course = course
    
    def get_info(self):
        self.checks()
        if isinstance(self.course, int):
            return f"Студент {self.name}, {self.age} років, {self.course} курс."
        else:
            return f"Студент {self.name}, {self.age} років, {self.course}."

    def change_course(self, new_course):
        self.course = new_course
        self.checks()

    def checks(self):
        self.check_me()
        self.check_course()

    def check_me(self):
        if self.age == 15 and self.course == 1 and self.name == "Олексій":
            self.course = "Відраховано на " + str(self.course) + " курсі" + " 😱"

    def check_course(self):
        if isinstance(self.course, int) and self.course > 4:
            self.course = "Відраховано з грамотою про закінчення навчання"

if __name__ == '__main__':
    game = GTA6()
    game.choice_file()
