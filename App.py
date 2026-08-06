import customtkinter as ctk
import pandas as pd

# Configuración del tema visual de CustomTkinter (Dark Mode)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# ==============================================================================
# 1. DATOS DE PRUEBA (O Carga desde SQLite / Pandas)
# ==============================================================================
raw_data = [
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_A1S", "campo": "Oficina", "interprete": "EIZM", "tvd": 10586.61, "md": 10586.61, "tvdss": -9639.61},
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_A2S", "campo": "Oficina", "interprete": "EIZM", "tvd": 11045.34, "md": 11045.34, "tvdss": -10098.34},
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_A3S", "campo": "Oficina", "interprete": "EIZM", "tvd": 11418.64, "md": 11418.64, "tvdss": -10471.64},
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_B1S", "campo": "Oficina", "interprete": "EIZM", "tvd": 11870.50, "md": 11870.50, "tvdss": -10923.50},
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_C1S", "campo": "Oficina", "interprete": "EIZM", "tvd": 12157.47, "md": 12157.47, "tvdss": -11210.47},
    {"muestra": "AGM-001", "uwi": "00108AGM0001X 01", "unidad": "Fs_Ofic_D1S", "campo": "Oficina", "interprete": "EIZM", "tvd": 12247.00, "md": 12247.00, "tvdss": -11300.00},
]

df = pd.DataFrame(raw_data)

# ==============================================================================
# 2. INTERFAZ GRÁFICA PRINCIPAL
# ==============================================================================
class StratigraphicColumnApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Visor Estratigráfico Offline — Local Desktop")
        self.geometry("1000x750")
        self.configure(fg_color="#0b0f19")  # Fondo ultra oscuro tipo dashboard

        # Contenedor Principal con padding
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # --- BARRA DE FILTROS Y CONTROLES ---
        self.create_filter_bar()

        # --- TARJETAS DE MÉTRICAS / KPI ---
        self.create_kpi_cards()

        # --- CABECERA DE LA COLUMNA ---
        self.header_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header_frame.pack(fill="x", pady=(15, 5))

        self.lbl_column_title = ctk.CTkLabel(
            self.header_frame, 
            text="Columna Litostratigráfica", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#38bdf8"
        )
        self.lbl_column_title.pack(side="left")

        # --- ÁREA DESPLAZABLE DE UNIDADES STRATIGRÁFICAS ---
        self.scrollable_column = ctk.CTkScrollableFrame(
            self.main_container,
            fg_color="#111827",
            corner_radius=12,
            border_width=1,
            border_color="#1f2937"
        )
        self.scrollable_column.pack(fill="both", expand=True, pady=10)

        # Cargar vista inicial
        self.actualizar_vista()

    def create_filter_bar(self):
        filter_frame = ctk.CTkFrame(self.main_container, fg_color="#111827", corner_radius=10, border_width=1, border_color="#1f2937")
        filter_frame.pack(fill="x", pady=(0, 15), ipady=5)

        # Selector de Muestra
        lbl_muestra = ctk.CTkLabel(filter_frame, text="MUESTRA SELECCIONADA:", font=ctk.CTkFont(size=11, weight="bold"), text_color="#9ca3af")
        lbl_muestra.grid(row=0, column=0, padx=(15, 5), pady=10, sticky="w")

        muestras = list(df["muestra"].unique())
        self.combo_muestra = ctk.CTkComboBox(filter_frame, values=muestras, command=lambda _: self.actualizar_vista(), fg_color="#1f2937", border_color="#374151")
        self.combo_muestra.set(muestras[0])
        self.combo_muestra.grid(row=0, column=1, padx=(0, 20), pady=10)

    def create_kpi_cards(self):
        kpi_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        kpi_frame.pack(fill="x", pady=(0, 10))

        # Tarjeta 1: Total Intervalos
        self.card_total = self._build_kpi_card(kpi_frame, "Registros Filtrados", "0", "#38bdf8")
        self.card_total.pack(side="left", fill="x", expand=True, padx=(0, 5))

        # Tarjeta 2: Profundidad Máxima
        self.card_max_tvd = self._build_kpi_card(kpi_frame, "TVD Máximo", "0.0 ft", "#34d399")
        self.card_max_tvd.pack(side="left", fill="x", expand=True, padx=5)

        # Tarjeta 3: TVDSS Máximo
        self.card_tvdss = self._build_kpi_card(kpi_frame, "TVDSS Máximo", "0.0 ft", "#c084fc")
        self.card_tvdss.pack(side="left", fill="x", expand=True, padx=(5, 0))

    def _build_kpi_card(self, parent, title, initial_val, color):
        card = ctk.CTkFrame(parent, fg_color="#111827", corner_radius=10, border_width=1, border_color="#1f2937")
        lbl_title = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=11), text_color="#9ca3af")
        lbl_title.pack(anchor="w", padx=12, pady=(8, 2))
        
        lbl_val = ctk.CTkLabel(card, text=initial_val, font=ctk.CTkFont(size=18, weight="bold"), text_color=color)
        lbl_val.pack(anchor="w", padx=12, pady=(0, 8))
        card.value_label = lbl_val
        return card

    def actualizar_vista(self):
        muestra_actual = self.combo_muestra.get()

        # 1. Filtrar Pandas por muestra y ORDENAR por TVD (Profundidad)
        df_filtrado = df[df["muestra"] == muestra_actual].copy()
        df_filtrado = df_filtrado.sort_values(by="tvd", ascending=True).reset_index(drop=True)

        # 2. Actualizar KPIs
        self.card_total.value_label.configure(text=f"{len(df_filtrado)}")
        if not df_filtrado.empty:
            max_tvd = df_filtrado["tvd"].max()
            max_tvdss = df_filtrado["tvdss"].min() # En TVDSS valores más negativos son más profundos
            self.card_max_tvd.value_label.configure(text=f"{max_tvd:.2f} ft")
            self.card_tvdss.value_label.configure(text=f"{max_tvdss:.2f} ft")

        # 3. Limpiar contenedor de lista
        for widget in self.scrollable_column.winfo_children():
            widget.destroy()

        # 4. Renderizar Tarjetas Litostratigráficas en Orden
        for index, row in df_filtrado.iterrows():
            diff_md_tvd = row["md"] - row["tvd"]
            self.crear_tarjeta_nivel(
                orden=index + 1,
                unidad=row["unidad"],
                campo=row["campo"],
                tvd=row["tvd"],
                md=row["md"],
                tvdss=row["tvdss"],
                diff=diff_md_tvd
            )

    def crear_tarjeta_nivel(self, orden, unidad, campo, tvd, md, tvdss, diff):
        # Frame Contenedor del Intervalo / Tope
        card = ctk.CTkFrame(
            self.scrollable_column, 
            fg_color="#1e293b", 
            corner_radius=8, 
            border_width=1, 
            border_color="#334155"
        )
        card.pack(fill="x", padx=10, pady=6, ipady=4)

        # 1. Círculo de Orden / Índice
        idx_frame = ctk.CTkFrame(card, width=32, height=32, corner_radius=16, fg_color="#0f172a")
        idx_frame.pack_propagate(False)
        idx_frame.pack(side="left", padx=12, pady=8)
        
        lbl_idx = ctk.CTkLabel(idx_frame, text=str(orden), font=ctk.CTkFont(size=12, weight="bold"), text_color="#94a3b8")
        lbl_idx.pack(expand=True)

        # 2. Nombre de la Unidad y Badge
        info_left = ctk.CTkFrame(card, fg_color="transparent")
        info_left.pack(side="left", padx=5, fill="both", expand=True)

        header_unit = ctk.CTkFrame(info_left, fg_color="transparent")
        header_unit.pack(anchor="w", pady=(4, 2))

        lbl_unit = ctk.CTkLabel(header_unit, text=unidad, font=ctk.CTkFont(size=14, weight="bold"), text_color="#f8fafc")
        lbl_unit.pack(side="left")

        # Badge del Campo
        badge_campo = ctk.CTkLabel(
            header_unit, 
            text=f" {campo} ", 
            font=ctk.CTkFont(size=10, weight="bold"), 
            fg_color="#0369a1", 
            text_color="#e0f2fe",
            corner_radius=4
        )
        badge_campo.pack(side="left", padx=10)

        # Subtítulo de Depths principales
        lbl_depths_left = ctk.CTkLabel(
            info_left, 
            text=f"TVD: {tvd:.2f} ft  |  MD: {md:.2f} ft", 
            font=ctk.CTkFont(size=11), 
            text_color="#94a3b8"
        )
        lbl_depths_left.pack(anchor="w")

        # 3. Datos Estratigráficos Derechos (TVDSS y Diff MD-TVD)
        info_right = ctk.CTkFrame(card, fg_color="transparent")
        info_right.pack(side="right", padx=15)

        lbl_tvdss = ctk.CTkLabel(
            info_right, 
            text=f"TVDSS: {tvdss:.2f} ft", 
            font=ctk.CTkFont(size=12, weight="bold"), 
            text_color="#2dd4bf"
        )
        lbl_tvdss.pack(anchor="e")

        lbl_diff = ctk.CTkLabel(
            info_right, 
            text=f"Diff MD-TVD: {diff:.2f}", 
            font=ctk.CTkFont(size=11), 
            text_color="#cbd5e1"
        )
        lbl_diff.pack(anchor="e")


if __name__ == "__main__":
    app = StratigraphicColumnApp()
    app.mainloop()
