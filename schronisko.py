import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime

#Kacper Rygielski, Albert Gumiński | WIT ITZ 2020/2021

pw_admin = {"login": "admin",
               "password": "admin"}  # implementacja logowania oraz loginy i hasla sa tymczasowe, aby zaobrazowac funkcjonalnosc aplikacji

pw_user = {"login": "user",
                "password": "user"}

class Shelter():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Schronisko")
        self.root.iconbitmap("./images/icon.ico")
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        self.user_password = tk.StringVar()
        self.user_login = tk.StringVar()
        self.create_login_view()

    def create_login_view(self):
        self.clear_screen()
        self.user_password.set('')
        self.user_login.set('')
        tk.Label(self.frame, text='Login: ').grid(row=0, column=0)
        login = tk.Entry(self.frame, textvariable=self.user_login)
        login.grid(row=0, column=1)
        tk.Label(self.frame, text='Hasło: ').grid(row=1, column=0)
        password = tk.Entry(self.frame, textvariable=self.user_password)
        password.grid(row=1, column=1)
        tk.Button(self.frame, text='Zaloguj się',
                  command=self.log_in).grid(row=2, column=1)

    def log_in(self):
        if self.user_password.get() == pw_admin['password'] and self.user_login.get() == pw_admin['login']:
            messagebox.showinfo('', 'Zalogowałeś się!')
            self.adminView()
        elif self.user_password.get() == pw_user['password'] and self.user_login.get() == pw_user['login']:
            messagebox.showinfo('', 'Zalogowałeś się!')
            self.userView()
        else:
            messagebox.showinfo('', 'Błędny login lub hasło!')

    def adminView(self):
        self.clear_screen()
        tk.Button(self.frame, text='Dodaj nowe zwierzę',
                  command=self.add_animal).grid(row=0, column=0)
        tk.Button(self.frame, text='Wyswietl zwierzęta przebywające aktualnie w schronisku',
                  command=self.show_animals).grid(row=1, column=0)
        tk.Button(self.frame, text='Edytuj profil zwierzęcia',
                  command=self.change_animal).grid(row=2, column=0)
        tk.Button(self.frame, text='Usuń zwierzę z bazy',
                  command=self.remove_animal).grid(row=3, column=0)
        tk.Button(self.frame, text='Wyświetl skargi od użytkowników',
                  command=self.show_complaints).grid(row=4, column=0)
        tk.Button(self.frame, text='Wyloguj',
                  command=self.create_login_view).grid(row=5, column=0)

    def userView(self):
        self.clear_screen()
        tk.Button(self.frame, text='Wyswietl dostepne zwierzęta do adopcji.',
                  command=self.show_animals2).grid(row=0, column=0)
        tk.Button(self.frame, text='Zamów próbny spacer',
                  command=self.order_trial_walk).grid(row=1, column=0)
        tk.Button(self.frame, text='Zarezerwuj adopcję',
                  command=self.booking_adoption).grid(row=2, column=0)
        tk.Button(self.frame, text='Złóż skargę',
                  command=self.complaint).grid(row=4, column=0)
        tk.Button(self.frame, text='Dodaj ogłoszenie o zgubieniu się zwierzęcia',
                  command=self.lost_notice).grid(row=5, column=0)
        tk.Button(self.frame, text='Wyloguj',
                  command=self.create_login_view).grid(row=6, column=0)
        
    def change_animal(self):
        def update_animal():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'UPDATE animals SET vaccinated = {vaccinated.get()} WHERE ID_animal = "{id_animal.get()}"'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='ID zwierzaka: ').grid(row=0, column=0)
        id_animal = tk.Entry(self.frame)
        id_animal.grid(row=0, column=1)
        tk.Label(self.frame, text='Zaszczepiony(1-tak|0-nie): ').grid(row=1, column=0)
        vaccinated = tk.Entry(self.frame)
        vaccinated.grid(row=1, column=1)
        tk.Button(self.frame, text='Zmodyfikuj',
                  command=update_animal).grid(row=2, column=1)
        tk.Button(self.frame, text='Wstecz',
                  command=self.adminView).grid(row=2, column=2)

    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def order_trial_walk(self):

        def trial_walk():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'INSERT INTO trial_walk (name, ID_animal, phone, date) VALUES("{name.get()}", "{id_animal.get()}", "{phone.get()}", "{date.get()}")'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='Imię i nazwisko: ').grid(row=0, column=0)
        name = tk.Entry(self.frame)
        name.grid(row=0, column=1)
        tk.Label(self.frame, text='ID zwierzęcia: ').grid(row=1, column=0)
        id_animal = tk.Entry(self.frame)
        id_animal.grid(row=1, column=1)
        tk.Label(self.frame, text='Telefon kontaktowy: ').grid(row=2, column=0)
        phone = tk.Entry(self.frame)
        phone.grid(row=2, column=1)
        tk.Label(
            self.frame, text='Proponowana data spaceru(rok-miesiąc-dzień): ').grid(row=3, column=0)
        date = tk.Entry(self.frame)
        date.grid(row=3, column=1)
        tk.Button(self.frame, text='Umów próbny spacer',
                  command=trial_walk).grid(row=4, column=1)
        tk.Button(self.frame, text='Wstecz',
                  command=self.userView).grid(row=4, column=2)

    def booking_adoption(self):

        def book():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            date_today = datetime.now().strftime('%Y-%m-%d')
            query = f'INSERT INTO reservations (ID_animal, name, species, date_of_reservation) VALUES("{animal_id.get()}", "{name.get()}", "{species.get()}", "{date_today}")'
            query2 = f'UPDATE animals SET reserved = 1 WHERE ID_animal = {animal_id.get()}'
            c.execute(query)
            c.execute(query2)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='ID zwierzaka: ').grid(row=0, column=0)
        animal_id = tk.Entry(self.frame)
        animal_id.grid(row=0, column=1)
        tk.Label(self.frame, text='Imie: ').grid(row=1, column=0)
        name = tk.Entry(self.frame)
        name.grid(row=1, column=1)
        tk.Label(self.frame, text='Gatunek: ').grid(row=2, column=0)
        species = tk.Entry(self.frame)
        species.grid(row=2, column=1)
        tk.Button(self.frame, text='Zarezerwuj zwierzaka',
                  command=book).grid(row=3, column=0)
        tk.Button(self.frame, text='Wstecz',
                  command=self.userView).grid(row=3, column=1)

    def complaint(self):

        def com():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'INSERT INTO complaint (name, surname, message) VALUES("{name.get()}", "{surname.get()}", "{message.get()}")'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='Imię: ').grid(row=0, column=0)
        name = tk.Entry(self.frame)
        name.grid(row=0, column=1)
        tk.Label(self.frame, text='Nazwisko: ').grid(row=1, column=0)
        surname = tk.Entry(self.frame)
        surname.grid(row=1, column=1)
        tk.Label(self.frame, text='Treść skargi: ').grid(row=2, column=0)
        message = tk.Entry(self.frame)
        message.grid(row=2, column=1)
        tk.Button(self.frame, text='Wyślij skargę',
                  command=com).grid(row=3, column=0)
        tk.Button(self.frame, text='Wstecz',
                  command=self.userView).grid(row=3, column=1)

    def lost_notice(self):

        def com():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'INSERT INTO lost_notice (message, name, date) VALUES("{message.get()}", "{name.get()}", "{date.get()}")'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='Treść ogłoszenia: ').grid(row=0, column=0)
        message = tk.Entry(self.frame)
        message.grid(row=0, column=1)
        tk.Label(self.frame, text='Podpis: ').grid(row=1, column=0)
        name = tk.Entry(self.frame)
        name.grid(row=1, column=1)
        tk.Label(self.frame, text='Data zagubienia się zwierzęcia(rok-miesiąc-dzień): ').grid(row=2, column=0)
        date = tk.Entry(self.frame)
        date.grid(row=2, column=1)
        tk.Button(self.frame, text='Wyślij ogłoszenie',
                  command=com).grid(row=3, column=0)
        tk.Button(self.frame, text='Wstecz',
                  command=self.userView).grid(row=3, column=1)

    def show_animals(self):

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = 'SELECT * FROM animals'
        results = c.execute(query)

        self.clear_screen()
        tk.Label(self.frame, text='ID zwierzęcia:').grid(row=0, column=0)
        tk.Label(self.frame, text='Imię:').grid(row=0, column=1)
        tk.Label(self.frame, text='Gatunek:').grid(row=0, column=2)
        tk.Label(self.frame, text='Rasa:').grid(row=0, column=3)
        tk.Label(self.frame, text='Szczepienie:').grid(row=0, column=4)
        tk.Label(self.frame, text='Data przyjęcia do schroniska:').grid(row=0, column=5)
        tk.Label(self.frame, text='Zarezerwowany:').grid(row=0, column=6)
        i = 1
        for result in results:
            tk.Label(self.frame, text=result[0]).grid(row=i, column=0)
            tk.Label(self.frame, text=result[1]).grid(row=i, column=1)
            tk.Label(self.frame, text=result[2]).grid(row=i, column=2)
            tk.Label(self.frame, text=result[3]).grid(row=i, column=3)
            vaccinated = "Tak"
            if (result[4]==0):
                vaccinated = "Nie"
            tk.Label(self.frame, text=vaccinated).grid(row=i, column=4)
            tk.Label(self.frame, text=result[5]).grid(row=i, column=5)
            tk.Label(self.frame, text=result[6]).grid(row=i, column=6)
            i += 1
        conn.close()
        tk.Button(self.frame, text='Wstecz',
                  command=self.adminView).grid(row=i+1, column=0)

    def show_animals2(self):

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = 'SELECT * FROM animals'
        results = c.execute(query)

        self.clear_screen()
        tk.Label(self.frame, text='ID zwierzęcia:').grid(row=0, column=0)
        tk.Label(self.frame, text='Imię:').grid(row=0, column=1)
        tk.Label(self.frame, text='Gatunek:').grid(row=0, column=2)
        tk.Label(self.frame, text='Rasa:').grid(row=0, column=3)
        tk.Label(self.frame, text='Szczepienie:').grid(row=0, column=4)
        tk.Label(self.frame, text='Data przyjęcia do schroniska:').grid(
            row=0, column=5)
        tk.Label(self.frame, text='Zarezerwowany:').grid(row=0, column=6)
        i = 1
        for result in results:
            tk.Label(self.frame, text=result[0]).grid(row=i, column=0)
            tk.Label(self.frame, text=result[1]).grid(row=i, column=1)
            tk.Label(self.frame, text=result[2]).grid(row=i, column=2)
            tk.Label(self.frame, text=result[3]).grid(row=i, column=3)
            vaccinated = "Tak"
            if (result[4] == 0):
                vaccinated = "Nie"

            tk.Label(self.frame, text=vaccinated).grid(row=i, column=4)
            tk.Label(self.frame, text=result[5]).grid(row=i, column=5)
            tk.Label(self.frame, text=result[5]).grid(row=i, column=6)
            i += 1
        conn.close()
        tk.Button(self.frame, text='Wstecz',command=self.userView).grid(row=i+1, column=0)

    def show_complaints(self):

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        query = 'SELECT * FROM complaint'
        results = c.execute(query)

        self.clear_screen()
        tk.Label(self.frame, text='ID skargi:').grid(row=0, column=0)
        tk.Label(self.frame, text='Imię:').grid(row=0, column=1)
        tk.Label(self.frame, text='Nazwisko:').grid(row=0, column=2)
        tk.Label(self.frame, text='Treść skargi:').grid(row=0, column=3)
        i = 1
        for result in results:
            tk.Label(self.frame, text=result[0]).grid(row=i, column=0)
            tk.Label(self.frame, text=result[1]).grid(row=i, column=1)
            tk.Label(self.frame, text=result[2]).grid(row=i, column=2)
            tk.Label(self.frame, text=result[3]).grid(row=i, column=3)
            i += 1
        conn.close()
        tk.Button(self.frame, text='Wstecz',
                  command=self.adminView).grid(row=i+1, column=0)
    
    def add_animal(self):

        date_today = datetime.now().strftime('%Y-%m-%d')
        var = tk.StringVar()

        def add_animal_post():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'INSERT INTO animals (name, species, breed, vaccinated, date_of_admission_to_the_shelter, reserved) VALUES("{name.get()}", "{species.get()}", "{breed.get()}", {var.get()}, "{date_today}", 0)'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()

        tk.Label(self.frame, text='Imię: ').grid(row=0, column=0)
        name = tk.Entry(self.frame)
        name.grid(row=0, column=1)
        tk.Label(self.frame, text='Gatunek: ').grid(row=1, column=0)
        species = tk.Entry(self.frame)
        species.grid(row=1, column=1)
        tk.Label(self.frame, text='Rasa:').grid(row=2, column=0)
        breed = tk.Entry(self.frame)
        breed.grid(row=2, column=1)
        tk.Label(self.frame, text='Szczepienie:' + var.get()).grid(row=3, column=0)
        vaccinated = tk.Radiobutton(self.frame, text="Tak", variable=var, value=1)
        vaccinated.grid(row=3, column=1)
        vaccinated2 = tk.Radiobutton(self.frame, text="Nie", variable=var, value=0)
        vaccinated2.grid(row=4, column=1)

        tk.Button(self.frame, text='Dodaj zwierzę do schroniska',
                  command=add_animal_post).grid(row=5, column=1)
        tk.Button(self.frame, text='Wstecz',
                  command=self.adminView).grid(row=6, column=1)

    def remove_animal(self):

        def delete_lek():
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            query = f'DELETE FROM animals WHERE ID_animal = "{id_animal.get()}"'
            c.execute(query)
            conn.commit()
            conn.close()

        self.clear_screen()
        tk.Label(self.frame, text='ID zwierzaka: ').grid(row=1, column=0)
        id_animal = tk.Entry(self.frame)
        id_animal.grid(row=1, column=1)
        tk.Button(self.frame, text='Usuń zwierzę ze schroniska',
                  command=delete_lek).grid(row=2, column=1)
        tk.Button(self.frame, text='Wstecz',
                  command=self.adminView).grid(row=2, column=2)

def main():
    app = Shelter()

main()