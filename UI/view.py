import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._lvOut = None
        self._btnIscrivi = None
        self._btnCercaCorsi = None
        self._btnCercaStudente = None
        self._txtNomeRead = None
        self._txtCognomeRead = None
        self._txtMatricolaIn = None
        self._btnCercaIscritti = None
        self._ddSelezioneCorso = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._ddSelezioneCorso=ft.Dropdown(label="Selezionare un corso", width=700)
        self._btnCercaIscritti=ft.ElevatedButton(text="Cerca iscritti", width=220,
                                                  on_click=self._controller.handleCercaIscritti)
        self._controller.fillddCorsi()

        row1=ft.Row([self._ddSelezioneCorso, self._btnCercaIscritti])

        self._txtMatricolaIn=ft.TextField(label="matricola", width=450)
        self._txtNomeRead=ft.TextField(label="nome", width=450, read_only=True)
        self._txtCognomeRead = ft.TextField(label="cognome", width=450, read_only=True)

        row2=ft.Row([self._txtMatricolaIn, self._txtNomeRead, self._txtCognomeRead])


        self._btnCercaStudente = ft.ElevatedButton(text="Cerca studente", width=220,
                                                   on_click=self._controller.handleCercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca corsi", width=220,
                                                   on_click=self._controller.handleCercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", width=220,
                                                   on_click=self._controller.handleIscrivi)

        row3=ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi])

        self._lvOut=ft.ListView(expand=True)

        self._page.add(row1,row2,row3, self._lvOut)




        """# button for the "hello" reply
        #self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)
        #row1 = ft.Row([self.txt_name, self.btn_hello],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()
        """
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
