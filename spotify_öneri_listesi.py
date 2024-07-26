import tkinter as tk
from tkinter import messagebox
import webbrowser


playlists = {
    ("Pop", "Mutlu", "Çalışma", "2000'ler", "Gitar", "Taylor Swift"): "https://open.spotify.com/playlist/1HhYaY0I4mW3YjvAN6Mm8t",
    ("Rock", "Üzgün", "Dinlenme", "90'lar", "Davul", "Nirvana"): "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
    ("Jazz", "Enerjik", "Egzersiz", "80'ler", "Saksafon", "Miles Davis"): "https://open.spotify.com/playlist/37i9dQZF1DXbITWG1ZJKYt",
    ("Hip-Hop", "Motivasyonel", "Yolculuk", "2010'lar", "Piyano", "Drake"): "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",
    ("Classical", "Rahat", "Dinlenme", "2020'ler", "Keman", "Ludovico Einaudi"): "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0",
    ("Pop", "Mutlu", "Egzersiz", "2010'lar", "Davul", "Taylor Swift"): "https://open.spotify.com/playlist/2fJGVa5iTnwV9KfjRfn3K7",
    ("Rock", "Enerjik", "Yolculuk", "80'ler", "Gitar", "Queen"): "https://open.spotify.com/playlist/37i9dQZF1DX2sUQwD7tbmL",
    ("Jazz", "Rahat", "Dinlenme", "90'lar", "Piyano", "Bill Evans"): "https://open.spotify.com/playlist/37i9dQZF1DXbITWG1ZJKYt",
    ("Hip-Hop", "Motivasyonel", "Çalışma", "2000'ler", "Davul", "Eminem"): "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0",
    ("Classical", "Üzgün", "Dinlenme", "2010'lar", "Keman", "Yo-Yo Ma"): "https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0",
    #! daha fazla liste eklemesi yapabilirsiniz
}

def cevaplari_gönder():
    
    tür = tür_var.get()
    mood = mood_var.get()
    aktivite = aktivite_var.get()
    cag_yil = cag_yil_var.get()
    enstürman = enstürman_var.get()
    sanatci = sanatci_var.get()

    
    önerilen_playlist(tür, mood, aktivite, cag_yil, enstürman, sanatci)

def önerilen_playlist(tür, mood, aktivite, cag_yil, enstürman, sanatci):
    key = (tür, mood, aktivite, cag_yil, enstürman, sanatci)
    if key in playlists:
        playlist_url = playlists[key]
        webbrowser.open(playlist_url)
    else:
        messagebox.showinfo("Sonuç", "Bu kriterlere uygun çalma listesi bulunamadı.")

root = tk.Tk()
root.title("Spotify Çalma Listesi Önerisi")


tk.Label(root, text="Hangi tür müzik dinlersiniz?").grid(row=0, column=0)
tür_var = tk.StringVar(value="Pop")
tür_options = ["Pop", "Rock", "Jazz", "Hip-Hop", "Classical"]
tür_menu = tk.OptionMenu(root, tür_var, *tür_options)
tür_menu.grid(row=0, column=1)


tk.Label(root, text="Şu anki ruh haliniz nedir?").grid(row=1, column=0)
mood_var = tk.StringVar(value="Mutlu")
mood_options = ["Mutlu", "Üzgün", "Enerjik", "Rahat", "Motivasyonel"]
mood_menu = tk.OptionMenu(root, mood_var, *mood_options)
mood_menu.grid(row=1, column=1)


tk.Label(root, text="Şu anda ne yapıyorsunuz?").grid(row=2, column=0)
aktivite_var = tk.StringVar(value="Çalışma")
aktivite_options = ["Çalışma", "Egzersiz", "Dinlenme", "Yolculuk", "Parti"]
aktivite_menu = tk.OptionMenu(root, aktivite_var, *aktivite_options)
aktivite_menu.grid(row=2, column=1)


tk.Label(root, text="Hangi dönemin müziğini tercih edersiniz?").grid(row=3, column=0)
cag_yil_var = tk.StringVar(value="2000'ler")
cag_yil_options = ["2020'ler", "2010'lar", "2000'ler", "90'lar", "80'ler"]
cag_yil_menu = tk.OptionMenu(root, cag_yil_var, *cag_yil_options)
cag_yil_menu.grid(row=3, column=1)


tk.Label(root, text="Hangi enstrüman öne çıksın?").grid(row=4, column=0)
enstürman_var = tk.StringVar(value="Gitar")
enstürman_options = ["Gitar", "Piyano", "Davul", "Keman", "Saksafon"]
enstürman_menu = tk.OptionMenu(root, enstürman_var, *enstürman_options)
enstürman_menu.grid(row=4, column=1)


tk.Label(root, text="Hangi sanatçıyı tercih edersiniz?").grid(row=5, column=0)
sanatci_var = tk.StringVar(value="Taylor Swift")
sanatci_options = ["Taylor Swift", "Nirvana", "Miles Davis", "Drake", "Ludovico Einaudi", "Queen", "Bill Evans", "Eminem", "Yo-Yo Ma"]
sanatci_menu = tk.OptionMenu(root, sanatci_var, *sanatci_options)
sanatci_menu.grid(row=5, column=1)

tk.Button(root, text="Öneri Al", command=cevaplari_gönder).grid(row=6, column=0, columnspan=2)

root.mainloop()
