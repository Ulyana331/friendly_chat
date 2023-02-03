import customtkinter
# створюємо клас App 
class App1(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App2(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{800}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App3(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{1740}+{0}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")

class App4(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{1740}+{800}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
class App5(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{900}+{400}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        
        
app1 = App1(400, 300)
app2 = App2(400, 300)
app3 = App3(400, 300)
app4 = App4(400, 300)
app5 = App5(400, 300)