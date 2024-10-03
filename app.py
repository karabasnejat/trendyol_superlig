import streamlit as st
import pandas as pd

# Başlık
st.title("Trendyol Süper Lig - 2024-2025 Sezonu")

# Sidebar'da bir seçim menüsü oluştur
menu = st.sidebar.selectbox(
    "Seçim Yapın",
    ["Lig Tablosu", "Gol Krallığı", "Maç Fikstürü"]
)

# Lig tablosu verisi
if menu == "Lig Tablosu":
    st.subheader("Trendyol Süper Lig 2024-2025 Puan Durumu")

    lig_tablo_data = {
        "Takım": [
            "GALATASARAY A.Ş.", "FENERBAHÇE A.Ş.", "BEŞİKTAŞ A.Ş.", "SAMSUNSPOR A.Ş.",
            "RAMS BAŞAKŞEHİR FUTBOL KULÜBÜ", "İKAS EYÜPSPOR", "GÖZTEPE A.Ş.", "SİPAY BODRUM FK",
            "CORENDON ALANYASPOR", "TRABZONSPOR A.Ş.", "TÜMOSAN KONYASPOR", "NET GLOBAL SİVASSPOR",
            "ANTALYASPOR A.Ş.", "KASIMPAŞA A.Ş.", "GAZİANTEP FUTBOL KULÜBÜ A.Ş.", "ÇAYKUR RİZESPOR A.Ş.",
            "BELLONA KAYSERİSPOR", "ATAKAŞ HATAYSPOR", "ADANA DEMİRSPOR A.Ş."
        ],
        "O": [7, 7, 6, 7, 6, 7, 6, 7, 7, 6, 7, 7, 7, 7, 6, 7, 6, 6, 7],
        "G": [6, 5, 5, 5, 4, 3, 2, 3, 2, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0],
        "B": [1, 1, 1, 0, 1, 3, 3, 0, 3, 5, 2, 2, 2, 4, 1, 1, 3, 2, 1],
        "M": [0, 1, 0, 2, 1, 1, 1, 4, 2, 0, 3, 3, 3, 2, 4, 5, 3, 4, 6],
        "A": [23, 16, 14, 11, 13, 12, 11, 8, 7, 6, 8, 6, 9, 9, 6, 3, 5, 4, 6],
        "Y": [8, 5, 4, 6, 8, 8, 7, 10, 9, 5, 10, 8, 14, 11, 10, 15, 12, 10, 17],
        "AV": [15, 11, 10, 5, 5, 4, 4, -2, -2, 1, -2, -2, -5, -2, -4, -12, -7, -6, -11],
        "P": [19, 16, 16, 15, 13, 12, 9, 9, 9, 8, 8, 8, 8, 7, 4, 4, 3, 2, 1]
    }

    lig_tablo = pd.DataFrame(lig_tablo_data)
    st.table(lig_tablo)

# Gol krallığı verisi
elif menu == "Gol Krallığı":
    st.subheader("2024-2025 Sezonu Gol Krallığı")

    gol_kralligi_data = {
        "Oyuncu": [
            "CIRO IMMOBILE", "EDIN DZEKO", "JOAO VITOR BRANDAO FIGUEIREDO", "BARIŞ ALPER YILMAZ",
            "BRAIAN JOSE SAMUDIO SEGOVIA", "DUSAN TADIC", "JULES OLIVIER NTCHAM", "KRZYSZTOF PIATEK",
            "NUNO MIGUEL DA COSTA JOIA", "DRIES MERTENS"
        ],
        "Takım": [
            "BEŞİKTAŞ A.Ş.", "FENERBAHÇE A.Ş.", "RAMS BAŞAKŞEHİR FUTBOL KULÜBÜ", "GALATASARAY A.Ş.",
            "ANTALYASPOR A.Ş.", "FENERBAHÇE A.Ş.", "SAMSUNSPOR A.Ş.", "RAMS BAŞAKŞEHİR FUTBOL KULÜBÜ",
            "KASIMPAŞA A.Ş.", "GALATASARAY A.Ş."
        ],
        "Gol Sayısı": [6, 5, 5, 4, 4, 4, 4, 4, 4, 3]
    }

    gol_kralligi = pd.DataFrame(gol_kralligi_data)
    st.table(gol_kralligi)

# Maç fikstürü
elif menu == "Maç Fikstürü":
    st.subheader("8. Hafta Maç Fikstürü")

    fikstur_data = {
        "Tarih": ["04.10.2024 20:00", "05.10.2024 13:30", "05.10.2024 16:00", "05.10.2024 19:00",
                  "05.10.2024 19:00", "06.10.2024 13:30", "06.10.2024 16:00", "06.10.2024 19:00",
                  "06.10.2024 19:00"],
        "Ev Sahibi": ["ÇAYKUR RİZESPOR A.Ş.", "KASIMPAŞA A.Ş.", "GÖZTEPE A.Ş.", "ATAKAŞ HATAYSPOR",
                      "RAMS BAŞAKŞEHİR FUTBOL KULÜBÜ", "TÜMOSAN KONYASPOR", "ADANA DEMİRSPOR A.Ş.",
                      "GALATASARAY A.Ş.", "GAZİANTEP FUTBOL KULÜBÜ A.Ş."],
        "Deplasman": ["ANTALYASPOR A.Ş.", "SİPAY BODRUM FK", "NET GLOBAL SİVASSPOR", "TRABZONSPOR A.Ş.",
                      "BELLONA KAYSERİSPOR", "İKAS EYÜPSPOR", "SAMSUNSPOR A.Ş.", "CORENDON ALANYASPOR",
                      "BEŞİKTAŞ A.Ş."]
    }

    fikstur = pd.DataFrame(fikstur_data)
    st.table(fikstur)
