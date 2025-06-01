import customtkinter as ctk
from PIL import Image
from Python_zvit_golovna.Python_zvit.windows import SeatSelectionWindow


class MatchCard:
    def __init__(self, parent, title, date, time, stadium, image_path, price):
        self.parent = parent
        self.title = title
        self.date = date
        self.time = time
        self.stadium = stadium
        self.image_path = image_path
        self.price = price
        self.create_card()

    def create_card(self):
        main_container = ctk.CTkFrame(self.parent, fg_color="transparent")
        main_container.pack(side="left", padx=15, pady=10)

        image_frame = ctk.CTkFrame(main_container)
        image_frame.pack(pady=(0, 10))

        try:
            image = Image.open(self.image_path)
            img = ctk.CTkImage(light_image=image, size=(300, 200))
            label_img = ctk.CTkLabel(image_frame, image=img, text='')
        except:
            label_img = ctk.CTkLabel(image_frame, text=f"Зображення не знайдено\n{self.image_path}", width=300,
                                     height=200, fg_color="gray75")
        label_img.pack(padx=5, pady=5)

        title_label = ctk.CTkLabel(image_frame, text=self.title, font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=5)

        date_label = ctk.CTkLabel(image_frame, text=f"Дата: {self.date}", font=ctk.CTkFont(size=16, weight="bold"))
        date_label.pack(pady=2)

        time_label = ctk.CTkLabel(image_frame, text=f"Час: {self.time}", font=ctk.CTkFont(size=16, weight="bold"))
        time_label.pack(pady=2)

        stadium_label = ctk.CTkLabel(image_frame, text=f"Стадіон: {self.stadium}",
                                     font=ctk.CTkFont(size=16, weight="bold"))
        stadium_label.pack(pady=2)

        price_label = ctk.CTkLabel(image_frame, text=f"Ціна за місце: {self.price} грн",
                                   font=ctk.CTkFont(size=16, weight="bold"), text_color="#1E8449")
        price_label.pack(pady=2)

        book_button = ctk.CTkButton(main_container, text="Забронювати місце", height=45, fg_color='#85a0ab',
                                    text_color='black', font=ctk.CTkFont(size=17, weight="bold"),
                                    command=lambda: SeatSelectionWindow(self.title, self.price))
        book_button.pack(pady=5, fill="x")