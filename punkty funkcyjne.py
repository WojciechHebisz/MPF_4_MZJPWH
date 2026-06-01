import tkinter as tk
from tkinter import ttk

def calculate_fp():
    # Pobieranie wartości z siatki (UFP)
    UFP = 0
    for i in range(5):
        for j in range(3):
            try:
                # Pobieramy wpisaną wartość, jeśli puste to 0
                val = int(frates_vars[i][j].get())
            except ValueError:
                val = 0
            UFP += val * wtFactors[i][j]

    # Pobieranie wartości z 14 suwaków (sumF)
    sumF = 0
    for i in range(14):
        sumF += aspects_vars[i].get()

    # Obliczenia końcowe
    CAF = 0.65 + (0.01 * sumF)
    FP = UFP * CAF

    # Aktualizacja wyników w oknie
    result_ufp.config(text=f"Unadjusted Function Points (UFP): {UFP}")
    result_caf.config(text=f"Complexity Adjustment Factor (CAF): {CAF:.2f}")
    result_fp.config(text=f"Function Points (FP): {FP:.2f}")

# Konfiguracja głównego okna
root = tk.Tk()
root.title("Kalkulator Punktów Funkcyjnych")
root.geometry("900x750")

# --- DANE BAZOWE ---
funUnits = [
    "External Inputs",
    "External Outputs",
    "External Inquiries",
    "Internal Logical Files",
    "External Interface Files"
]
wtRates = ["Low", "Average", "High"]
wtFactors = [
    [3, 4, 6],
    [4, 5, 7],
    [3, 4, 6],
    [7, 10, 15],
    [5, 7, 10]
]
aspects = [
    "reliable backup and recovery required ?",
    "data communication required ?",
    "are there distributed processing functions ?",
    "is performance critical ?",
    "will the system run in an existing heavily utilized operational environment ?",
    "on line data entry required ?",
    "does the on line data entry require the input transaction to be built over multiple screens ?",
    "are the master files updated on line ?",
    "is the inputs, outputs, files or inquiries complex ?",
    "is the internal processing complex ?",
    "is the code designed to be reusable ?",
    "are the conversion and installation included in the design ?",
    "is the system designed for multiple installations in different organizations ?",
    "is the application designed to facilitate change and ease of use by the user ?"
]

# Domyślne wartości z Twojego kodu C++
default_frates = [
    [0, 50, 0],
    [0, 40, 0],
    [0, 35, 0],
    [0, 6, 0],
    [0, 4, 0]
]

# --- BUDOWA INTERFEJSU ---
# Ramka główna podzielona na lewą (tabela) i prawą (suwaki) stronę
left_frame = ttk.Frame(root, padding="10")
left_frame.grid(row=0, column=0, sticky="nsew")

right_frame = ttk.Frame(root, padding="10")
right_frame.grid(row=0, column=1, sticky="nsew")

# --- LEWA STRONA: Tabela (frates) ---
ttk.Label(left_frame, text="Wprowadź wartości funkcyjne:", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, pady=(0, 10))

# Nagłówki kolumn (Low, Average, High)
for j, rate in enumerate(wtRates):
    ttk.Label(left_frame, text=rate, font=("Arial", 10, "bold")).grid(row=1, column=j+1, padx=5, pady=5)

frates_vars = [] # Lista przechowująca zmienne wpisywane przez użytkownika

for i, unit in enumerate(funUnits):
    # Nazwy wierszy
    ttk.Label(left_frame, text=unit).grid(row=i+2, column=0, sticky="w", padx=5, pady=5)
    
    row_vars = []
    for j in range(3):
        var = tk.StringVar(value=str(default_frates[i][j])) # Ustawiamy domyślne wartości
        entry = ttk.Entry(left_frame, textvariable=var, width=5, justify="center")
        entry.grid(row=i+2, column=j+1, padx=5, pady=5)
        row_vars.append(var)
    frates_vars.append(row_vars)

# Sekcja wyników po lewej stronie (pod tabelą)
ttk.Label(left_frame, text="Wyniki Analizy:", font=("Arial", 12, "bold")).grid(row=8, column=0, columnspan=4, pady=(30, 10))

result_ufp = ttk.Label(left_frame, text="Unadjusted Function Points (UFP): 0", font=("Arial", 11))
result_ufp.grid(row=9, column=0, columnspan=4, sticky="w", pady=2)

result_caf = ttk.Label(left_frame, text="Complexity Adjustment Factor (CAF): 0.00", font=("Arial", 11))
result_caf.grid(row=10, column=0, columnspan=4, sticky="w", pady=2)

result_fp = ttk.Label(left_frame, text="Function Points (FP): 0.00", font=("Arial", 11, "bold"), foreground="blue")
result_fp.grid(row=11, column=0, columnspan=4, sticky="w", pady=2)

# Przycisk "Oblicz"
calc_btn = ttk.Button(left_frame, text="Oblicz Punkty Funkcyjne", command=calculate_fp)
calc_btn.grid(row=12, column=0, columnspan=4, pady=(20, 0), sticky="ew")


# --- PRAWA STRONA: 14 Suwaków (aspects) ---
ttk.Label(right_frame, text="Oceń 14 czynników złożoności (0 - 5):", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

aspects_vars = [] # Zmienne przechowujące wartości z suwaków

for i, aspect in enumerate(aspects):
    # Etykieta z pytaniem
    ttk.Label(right_frame, text=f"{i+1}. {aspect}", wraplength=400).grid(row=i*2+1, column=0, columnspan=2, sticky="w", pady=(5, 0))
    
    # Zmienna powiązana z suwakiem (domyślnie ustawiona na 3, tak jak 'fac_rate' w Twoim kodzie)
    var = tk.IntVar(value=3)
    aspects_vars.append(var)
    
    # Suwak (Scale) od 0 do 5
    slider = ttk.Scale(right_frame, from_=0, to=5, orient="horizontal", variable=var, length=200)
    # W tk.Scale trzeba użyć komendy do aktualizacji wyświetlanej wartości przy przesunięciu
    slider.grid(row=i*2+2, column=0, sticky="w", padx=(10, 0))
    
    # Numeryczny podgląd aktualnej wartości suwaka
    val_label = ttk.Label(right_frame, text="3")
    val_label.grid(row=i*2+2, column=1, sticky="w", padx=(5, 0))
    
    # Funkcja aktualizująca tekst z cyfrą obok suwaka na żywo
    def update_label(event, v=var, l=val_label):
        l.config(text=str(round(v.get())))
    
    slider.bind("<Motion>", update_label)
    slider.bind("<ButtonRelease-1>", update_label)

# Wykonaj pierwsze obliczenie przy starcie, aby wypełnić wyniki domyślnymi wartościami
calculate_fp()

# Start pętli głównej okna
root.mainloop()