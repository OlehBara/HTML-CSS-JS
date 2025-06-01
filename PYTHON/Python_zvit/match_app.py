import customtkinter as ctk
from Python_zvit_golovna.Python_zvit.match_card import MatchCard
from Python_zvit_golovna.Python_zvit.windows import BookingsWindow


class MatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Бронювання мачів на футбол")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        ctk.set_appearance_mode('dark')

        title_label = ctk.CTkLabel(self.root, text="Обери матч", font=ctk.CTkFont(size=36, weight="bold"))
        title_label.pack(pady=20)

        bookings_btn = ctk.CTkButton(self.root, text="Мої бронювання", fg_color="#9bbcf4", text_color="black",
                                     font=ctk.CTkFont(size=16, weight="bold"), width=150, height=40,
                                     command=lambda: BookingsWindow(self.root))
        bookings_btn.pack(pady=10)

        scroll_frame = ctk.CTkScrollableFrame(self.root, fg_color="#2e3336")
        scroll_frame.pack(padx=20, pady=10, fill="both", expand=True)

        row1_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row1_frame.pack(pady=15)

        MatchCard(row1_frame, "Мілан - Інтер", "25 травня 2025", "20:00", "Сан-Сіро", "Python_zvit/image/inter.jpg", 1200)
        MatchCard(row1_frame, "Динамо Київ - Шахтар", "28 травня 2025", "19:30", "НСК Олімпійський",
                  "Python_zvit/image/dinamo.jpeg", 700)
        MatchCard(row1_frame, "Барселона - Реал Мадрид", "1 червня 2025", "21:00", "Камп Ноу", "Python_zvit/image/barca.jpg", 1500)
        MatchCard(row1_frame, "Рух - Карпати Львів", "5 червня 2025", "17:00", "Арена Львів", "Python_zvit/image/hq720 1.png", 500)


        row2_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row2_frame.pack(pady=15)

        MatchCard(row2_frame, "Баварія - Боруссія Дортмунд", "12 червня 2025", "20:30", "Альянц Арена",
                  "Python_zvit/image/poster7.jpg", 1000)
        MatchCard(row2_frame, "Манчестер Юнайтед - Ліверпуль", "15 червня 2025", "18:00", "Олд Траффорд",
                  "Python_zvit/image/34544441216b1a2b81b96f1d1a87faa0-quality_70Xresize_1Xallow_enlarge_0Xw_835Xh_0.jpg", 1200)
        MatchCard(row2_frame, "ПСЖ - Марсель", "19 червня 2025", "21:00", "Парк де Пренс", "Python_zvit/image/psg.jpg", 900)
        MatchCard(row2_frame, "Манчестер Сіті - Челсі", "23 червня 2025", "16:00", "Етіхад",
                  "Python_zvit/image/abS0ppxUJ_1290x760__1.jpg", 1000)


        row3_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row3_frame.pack(pady=15)

        MatchCard(row3_frame, "Аякс - Фейєнорд", "26 червня 2025", "18:30", "Йохан Кройф Арена", "Python_zvit/image/ajax.png", 800)
        MatchCard(row3_frame, "Арсенал - Тоттенгем", "30 червня 2025", "20:45", "Емірейтс", "Python_zvit/image/arsenal.jpg", 1300)
        MatchCard(row3_frame, "Галатасарай - Фенербахче", "3 липня 2025", "19:00", "РамС Парк", "Python_zvit/image/galatasaray.jpg",700)
        MatchCard(row3_frame, "Бенфіка - Порту", "6 липня 2025", "21:15", "Ештадіу да Луж", "Python_zvit/image/portu.png", 900)

        row4_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row4_frame.pack(pady=15)

        MatchCard(row4_frame, "Ювентус - Наполі", "10 липня 2025", "21:00", "Альянц Стадіум", "Python_zvit/image/napoli.jpg", 1000)
        MatchCard(row4_frame, "Рома - Лаціо", "14 липня 2025", "19:30", "Стадіо Олімпіко", "Python_zvit/image/roma.jpg", 950)
        MatchCard(row4_frame, "Селтік - Рейнджерс", "17 липня 2025", "16:00", "Селтік Парк", "Python_zvit/image/celtic.png", 700)
        MatchCard(row4_frame, "Аль-Наср - Аль-Хіляль", "20 липня 2025", "20:00", "Кінг Сауд", "Python_zvit/image/nasr.png", 1000)
