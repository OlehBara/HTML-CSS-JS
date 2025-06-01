import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox
import json
from datetime import datetime


class PaymentWindow:
    def __init__(self, match_title, price, selected_seats):
        self.window = ctk.CTkToplevel()
        self.window.title("Сплатити за матч")
        self.window.geometry("600x800")
        self.window.attributes("-topmost", True)
        self.window.after(10, lambda: self.window.attributes('-topmost', False))

        total_price = price * len(selected_seats)

        try:
            photo = Image.open("Python_zvit/image/image 18.png")
            photo_img = ctk.CTkImage(light_image=photo, size=(500, 450))
            photo_label = ctk.CTkLabel(self.window, image=photo_img, text="")
            photo_label.pack(pady=10)
        except:
            photo_label = ctk.CTkLabel(self.window, text="...-", fg_color="gray75")
            photo_label.pack(pady=10, fill="both", expand=True)

        form_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)

        title = ctk.CTkLabel(form_frame,
                             text=f"Сплатити за матч\nДо сплати: {total_price} грн (за {len(selected_seats)} місця)",
                             font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(pady=10)

        card_label = ctk.CTkLabel(form_frame, text="Номер вашої карти:", font=ctk.CTkFont(size=16, weight="bold"))
        card_label.pack(pady=5)

        card_entry = ctk.CTkEntry(form_frame, width=300, height=40, placeholder_text="Наприклад: 4441 4566 2312 4356")
        card_entry.pack(pady=5)

        # Функція підтвердження оплати
        def confirm_payment():
            card_number = card_entry.get().strip()
            if not card_number:
                CTkMessagebox(title="Помилка", message="Будь ласка, введіть коректний номер карти (16 цифр)!",
                              icon="cancel")
                return
            if len(card_number.replace(" ", "")) != 16:
                CTkMessagebox(title="Помилка", message="Будь ласка, введіть коректний номер карти (16 цифр)!",
                              icon="cancel")
                return
            if not card_number.replace(" ", "").isdigit():
                CTkMessagebox(title="Помилка", message="Будь ласка, введіть коректний номер карти (16 цифр)!",
                              icon="cancel")
                return

            CTkMessagebox(title="Успіх", message="Оплата успішно проведена!", icon="check")
            self.window.after(100, self.window.destroy)

        button_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        pay_btn = ctk.CTkButton(button_frame, text="Сплатити", fg_color="#d3d3d3", text_color="black",
                                hover_color="#a9a9a9", font=ctk.CTkFont(size=16, weight="bold"), width=200, height=40,
                                command=confirm_payment)
        pay_btn.pack(side="left", padx=10)

        cancel_btn = ctk.CTkButton(button_frame, text="Скасувати платіж", fg_color="#e57373", text_color="black",
                                   hover_color="#b71c1c", font=ctk.CTkFont(size=16, weight="bold"), width=200,
                                   height=40, command=lambda: self.window.after(100, self.window.destroy))
        cancel_btn.pack(side="left", padx=10)


class BookingsWindow:
    def __init__(self, parent):
        self.window = ctk.CTkToplevel(parent)
        self.window.title("Мої бронювання")
        self.window.geometry("800x600")
        self.window.attributes("-topmost", True)
        self.window.after(10, lambda: self.window.attributes('-topmost', False))

        scroll_frame = ctk.CTkScrollableFrame(self.window, fg_color="transparent")
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

        title = ctk.CTkLabel(scroll_frame, text="Список ваших бронювань", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(pady=15)

        try:
            f = open("Python_zvit/bookings.json", "r", encoding="utf-8")
            bookings = json.load(f)
            f.close()
        except:
            bookings = []

        if len(bookings) == 0:
            no_bookings_label = ctk.CTkLabel(scroll_frame, text="У вас ще немає бронювань.", font=ctk.CTkFont(size=16))
            no_bookings_label.pack(pady=10)
        else:
            for booking in bookings:
                booking_frame = ctk.CTkFrame(scroll_frame, fg_color="#333333", corner_radius=10)
                booking_frame.pack(pady=5, padx=10, fill="x")

                booking_text = f"Матч: {booking['match_title']}\nМісця: {', '.join(booking['seats'])}\nІм'я: {booking['name']}\nПрізвище: {booking['surname']}\nEmail: {booking['email']}\nДата бронювання: {booking['booking_time']}"

                booking_label = ctk.CTkLabel(booking_frame, text=booking_text, font=ctk.CTkFont(size=14), anchor="w",
                                             justify="left")
                booking_label.pack(padx=10, pady=10, fill="x")

        close_btn = ctk.CTkButton(scroll_frame, text="Закрити", fg_color="#e57373", text_color="black",
                                  font=ctk.CTkFont(size=16, weight="bold"), width=130, height=40,
                                  command=lambda: self.window.after(100, self.window.destroy))
        close_btn.pack(pady=20)


class SeatSelectionWindow:
    def __init__(self, match_title, price):
        self.match_title = match_title
        self.price = price
        self.window = ctk.CTkToplevel()
        self.window.title(f"Вибір місця: {match_title}")
        self.window.state("zoomed")
        self.window.attributes("-topmost", True)
        self.window.after(10, lambda: self.window.attributes('-topmost', False))
        self.seat_buttons = {}
        self.seat_states = {}
        self.selected_seats = []
        self.total_price = 0
        self.booked_seats = self.get_booked_seats()

        scroll_frame = ctk.CTkScrollableFrame(self.window, fg_color="transparent")
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

        title = ctk.CTkLabel(scroll_frame, text=f"Виберіть місце на матч {match_title}",
                             font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(pady=15)

        self.price_label = ctk.CTkLabel(scroll_frame, text=f"Загальна ціна: {self.total_price} грн",
                                       font=ctk.CTkFont(size=18, weight="bold"), text_color="#1E8449")
        self.price_label.pack(pady=5)

        top_rows_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        top_rows_frame.pack(pady=10)

        top_row_letters = ['A', 'B', 'C', 'D', 'E', 'M', 'N', 'O', 'P']
        for letter in top_row_letters:
            row_frame = ctk.CTkFrame(top_rows_frame, fg_color="transparent")
            row_frame.pack(pady=3)
            for num in range(1, 16):
                seat_id = f"{letter}{num}"
                is_booked = seat_id in self.booked_seats

                if is_booked:
                    fg_color = "#FF0000"
                    hover_color = "#FF0000"
                    btn_state = "disabled"
                    btn_command = None
                else:
                    fg_color = "#7447d6"
                    hover_color = "#45B39D"
                    btn_state = "normal"
                    btn_command = lambda sid=seat_id: self.toggle_seat(sid)

                seat_btn = ctk.CTkButton(
                    row_frame,
                    text=seat_id,
                    width=40,
                    height=20,
                    corner_radius=6,
                    fg_color=fg_color,
                    hover_color=hover_color,
                    font=ctk.CTkFont(size=12, weight="bold"),
                    command=btn_command,
                    state=btn_state
                )
                seat_btn.pack(side="left", padx=3)
                self.seat_buttons[seat_id] = seat_btn
                self.seat_states[seat_id] = False

        field = ctk.CTkLabel(scroll_frame, text='Стадіон', width=900, height=315, corner_radius=180, fg_color="#6e7d70",
                             text_color="black", font=ctk.CTkFont(size=26, weight="bold"))
        field.pack(pady=10)

        bottom_rows_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        bottom_rows_frame.pack(pady=10)

        bottom_row_letters = ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'Q', 'R']
        for letter in bottom_row_letters:
            row_frame = ctk.CTkFrame(bottom_rows_frame, fg_color="transparent")
            row_frame.pack(pady=3)
            for num in range(1, 16):
                seat_id = f"{letter}{num}"
                is_booked = seat_id in self.booked_seats

                if is_booked:
                    fg_color = "#FF0000"
                    hover_color = "#FF0000"
                    btn_state = "disabled"
                    btn_command = None
                else:
                    fg_color = "#1f3aed"
                    hover_color = "#45B39D"
                    btn_state = "normal"
                    btn_command = lambda sid=seat_id: self.toggle_seat(sid)

                seat_btn = ctk.CTkButton(
                    row_frame,
                    text=seat_id,
                    width=40,
                    height=20,
                    corner_radius=6,
                    fg_color=fg_color,
                    hover_color=hover_color,
                    font=ctk.CTkFont(size=12, weight="bold"),
                    command=btn_command,
                    state=btn_state
                )
                seat_btn.pack(side="left", padx=3)
                self.seat_buttons[seat_id] = seat_btn
                self.seat_states[seat_id] = False

        button_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        back_btn = ctk.CTkButton(button_frame, text="Назад", fg_color="#e57373", text_color="black",
                                 font=ctk.CTkFont(size=18, weight="bold"), width=130, height=45,
                                 command=lambda: self.window.after(100, self.window.destroy))
        back_btn.pack(side="left", padx=10)

        next_btn = ctk.CTkButton(button_frame, text="Далі", fg_color="#9bbcf4", text_color="black",
                                 font=ctk.CTkFont(size=18, weight="bold"), width=130, height=45,
                                 command=lambda: self.show_registration(self.price))
        next_btn.pack(side="left", padx=10)

    # Метод для отримання заброньованих місць для поточного матчу
    def get_booked_seats(self):
        booked_seats = set()
        try:
            with open("Python_zvit/bookings.json", "r", encoding="utf-8") as f:
                bookings = json.load(f)
                for booking in bookings:
                    if booking["match_title"] == self.match_title:
                        booked_seats.update(booking["seats"])
        except:
            pass
        return booked_seats

    # Функція для вибору/скасування місця з оновленням ціни
    def toggle_seat(self, seat_id):
        if seat_id in self.booked_seats:
            return

        self.seat_states[seat_id] = not self.seat_states[seat_id]
        if self.seat_states[seat_id]:
            self.selected_seats.append(seat_id)
        else:
            self.selected_seats.remove(seat_id)

        button = self.seat_buttons[seat_id]
        if self.seat_states[seat_id]:
            button.configure(fg_color="#FF0000")
        else:
            if seat_id[0] in ['A', 'B', 'C', 'D', 'E', 'M', 'N', 'O', 'P']:
                button.configure(fg_color="#7447d6")
            else:
                button.configure(fg_color="#1f3aed")

        self.total_price = self.price * len(self.selected_seats)
        self.price_label.configure(text=f"Загальна ціна: {self.total_price} грн")

    # Функція показу реєстрації
    def show_registration(self, price):
        if not any(self.seat_states.values()):
            CTkMessagebox(title="Помилка", message="Спочатку виберіть місця!", icon="cancel")
            return

        registration_window = ctk.CTkToplevel(self.window)
        registration_window.title("Реєстрація")
        registration_window.geometry("950x620")
        registration_window.attributes("-topmost", True)
        registration_window.after(10, lambda: registration_window.attributes('-topmost', False))

        photo_frame = ctk.CTkFrame(registration_window, width=300, height=500, fg_color="transparent")
        photo_frame.pack(side="left", fill="y")
        try:
            photo = Image.open("Python_zvit/image/image 17.png")
            photo_img = ctk.CTkImage(light_image=photo, size=(500, 500))
            photo_label = ctk.CTkLabel(photo_frame, image=photo_img, text="")
            photo_label.pack(fill="both", expand=True)
        except:
            photo_label = ctk.CTkLabel(photo_frame, text="Фото не знайдено", fg_color="gray75")
            photo_label.pack(fill="both", expand=True)

        form_frame = ctk.CTkFrame(registration_window, fg_color="transparent")
        form_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(form_frame,
                             text=f"Бронювання місця на матч\n{self.match_title}\n-------------------------------------------",
                             font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=10)

        if self.selected_seats:
            selected_seats_text = "Ви обрали місце: " + ", ".join(self.selected_seats)
        else:
            selected_seats_text = "Ви не обрали жодного місця"

        seats_label = ctk.CTkLabel(form_frame, text=selected_seats_text, font=ctk.CTkFont(size=16, weight="bold"))
        seats_label.pack(pady=5)

        total_price = self.total_price
        price_label = ctk.CTkLabel(form_frame, text=f"Ціна: {total_price} грн",
                                   font=ctk.CTkFont(size=16, weight="bold"), text_color="#1E8449")
        price_label.pack(pady=5)

        name_label = ctk.CTkLabel(form_frame, text="Введіть своє ім'я:", font=ctk.CTkFont(size=16, weight="bold"))
        name_label.pack(pady=5)
        name_entry = ctk.CTkEntry(form_frame, width=300, height=40, placeholder_text="Ім'я")
        name_entry.pack(pady=5)

        surname_label = ctk.CTkLabel(form_frame, text="Введіть своє прізвище:",
                                     font=ctk.CTkFont(size=16, weight="bold"))
        surname_label.pack(pady=5)
        surname_entry = ctk.CTkEntry(form_frame, width=300, height=40, placeholder_text='Прізвище')
        surname_entry.pack(pady=5)

        email_label = ctk.CTkLabel(form_frame, text="Введіть свій email:", font=ctk.CTkFont(size=16, weight="bold"))
        email_label.pack(pady=5)
        email_entry = ctk.CTkEntry(form_frame, width=300, height=40, placeholder_text='email')
        email_entry.pack(pady=5)

        # Функція збереження бронювання
        def submit_booking():
            name = name_entry.get().strip()
            surname = surname_entry.get().strip()
            email = email_entry.get().strip()

            if not name or not surname or not email:
                CTkMessagebox(title="Помилка", message="Будь ласка, заповніть усі поля!", icon="cancel")
                return

            booking = {
                "match_title": self.match_title,
                "seats": self.selected_seats,
                "name": name,
                "surname": surname,
                "email": email,
                "booking_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            try:
                f = open("Python_zvit/bookings.json", "r", encoding="utf-8")
                bookings = json.load(f)
                f.close()
            except:
                bookings = []

            bookings.append(booking)

            f = open("Python_zvit/bookings.json", "w", encoding="utf-8")
            json.dump(bookings, f, ensure_ascii=False, indent=4)
            f.close()

            PaymentWindow(self.match_title, self.price, self.selected_seats)
            registration_window.after(100, registration_window.destroy)

        pay_btn = ctk.CTkButton(form_frame, text="Сплатити", fg_color="white", text_color="black",
                                hover_color='#687580', font=ctk.CTkFont(size=16, weight="bold"), width=200, height=40,
                                command=submit_booking)
        pay_btn.pack(pady=20)

        back_btn = ctk.CTkButton(form_frame, text="Назад", fg_color="#e57373", text_color="black",
                                 hover_color='#687580', font=ctk.CTkFont(size=16, weight="bold"), width=130, height=40,
                                 command=lambda: registration_window.after(100, registration_window.destroy))
        back_btn.pack(pady=10)

        ctk.set_appearance_mode("dark")