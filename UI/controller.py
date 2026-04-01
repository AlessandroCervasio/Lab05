import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillddCorsi(self):
        lista=self._model.getAllCorsi()
        for i in lista:
            self._view._ddSelezioneCorso.options.append(ft.dropdown.Option(key=i.codIns,
                                                                           data=i,
                                                                           text=str(i),
                                                                           ))

    def handleCercaIscritti(self, e):
        codins=self._view._ddSelezioneCorso.value
        listaIscritti=self._model.getStudentiDiUnCorso(codins)
        if codins is None:
            self._view.create_alert("Selezionare un corso!")
            return
        else:
            if len(listaIscritti)!=0:
                for i in listaIscritti:
                    self._view._lvOut.controls.append(ft.Text(f"{i}"))
            else:
                self._view._lvOut.controls.append(ft.Text(f"Nessun utente iscritto al corso selezionato"))
        self._view.update_page()

    def handleCercaStudente(self, e):
        matricola= self._view._txtMatricolaIn.value
        studente=self._model.getStudenteConMatricola(matricola)
        if matricola is None or matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        else:
            self._view._txtNomeRead.value=studente.nome
            self._view._txtCognomeRead.value=studente.cognome


        self._view.update_page()


    def handleCercaCorsi(self, e):
        pass
    def handleIscrivi(self, e):
        pass

