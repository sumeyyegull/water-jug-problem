from collections import deque

# EBOB (GCD) hesaplama fonksiyonu
def ebob(a, b):
    """
    Bu fonksiyon, iki sayı arasındaki en büyük ortak böleni (EBOB) hesaplar.
    EBOB, iki sayının bölenleri arasındaki en büyük sayıdır.
    Bu problemde, hedef hacmin elde edilebilir olup olmadığını kontrol etmek için kullanılır.

    a: Birinci sayıyı alır.
    b: İkinci sayıyı alır.

    return: a ve b arasındaki en büyük ortak bölen değeri
    """
    if b == 0:
        return a
    return ebob(b, a % b)  # Öklid algoritması ile EBOB hesaplama

# BFS (Genişlik Öncelikli Arama) ile çözüm bulma
def bfs_agaci(a_kapasite, b_kapasite, hedef):
    """
    Bu fonksiyon, BFS algoritmasını kullanarak verilen su şişe kapasite değerlerine 
    ulaşmak için gerekli adımları çözer. Genişlik öncelikli arama, tüm geçerli durumları 
    seviyeli bir şekilde keşfeder.

    a_kapasite: A şişesinin kapasitesini alır.
    b_kapasite: B şişesinin kapasitesini alır.
    hedef: Hedeflenen hacmi belirtir.

    return: Hedef hacme ulaşan çözüm yolunu döndürür.
    """
    ziyaret_edilenler = set()  # Daha önce ziyaret edilen durumları saklamak için bir küme
    kuyruk = deque()  # BFS'de kullanılacak olan kuyruk yapısı
    ebeveyn_haritasi = {}  # Her durumun önceki durumunu saklayarak çözüm yolu oluşturmak için

    baslangic = (0, 0)  # Başlangıç durumu: (0, 0) yani her iki şişe de boş
    kuyruk.append(baslangic)  # Başlangıç durumunu kuyruğa ekle
    ziyaret_edilenler.add(baslangic)  # Başlangıç durumunu ziyaret edilmiş olarak işaretle
    ebeveyn_haritasi[baslangic] = None  # Başlangıç durumunun ebeveyni yok

    print("\n[BFS Arama Ağacı]")

    while kuyruk:
        mevcut = kuyruk.popleft()  # Kuyruğun başından bir durum al
        a, b = mevcut

        print(f"Mevcut Durum: {mevcut}")  # Mevcut durumu ekrana yazdır

        # Hedefe ulaşıldıysa, yolu geri izleyerek oluştur
        if a == hedef or b == hedef:
            yol = []  # Hedefe ulaşmak için yol listesi
            while mevcut is not None:
                yol.append(mevcut)  # Yolu oluştur
                mevcut = ebeveyn_haritasi[mevcut]  # Önceki durumu al
            return yol[::-1]  # Yolu ters çevirerek başlangıçtan sona doğru getir

        # Olası tüm sonraki durumları dene
        sonraki_durumlar = [
            (a_kapasite, b),  # A şişesini doldur
            (a, b_kapasite),  # B şişesini doldur
            (0, b),           # A şişesini boşalt
            (a, 0),           # B şişesini boşalt
            (a - min(a, b_kapasite - b), b + min(a, b_kapasite - b)),  # A'dan B'ye dök
            (a + min(b, a_kapasite - a), b - min(b, a_kapasite - a))   # B'den A'ya dök
        ]

        for durum in sonraki_durumlar:
            if durum not in ziyaret_edilenler:
                ziyaret_edilenler.add(durum)  # Durumu ziyaret et
                ebeveyn_haritasi[durum] = mevcut  # Ebeveyn haritasına ekle
                kuyruk.append(durum)  # Durumu kuyruğa ekle

    return None  # Hedefe ulaşmak mümkün değilse None döndür

# DFS (Derinlik Öncelikli Arama) ile çözüm bulma
def dfs_agaci(a_kapasite, b_kapasite, hedef):
    """
    Bu fonksiyon, DFS algoritmasını kullanarak verilen su şişe kapasite değerlerine 
    ulaşmak için gerekli adımları çözer. Derinlik öncelikli arama, ilk keşfedilen 
    geçerli durumu derinlemesine keşfeder.

    a_kapasite: A şişesinin kapasitesini alır.
    b_kapasite: B şişesinin kapasitesini alır.
    hedef: Hedeflenen hacmi belirtir.

    return: Hedef hacme ulaşan çözüm yolunu döndürür.
    """
    ziyaret_edilenler = set()  # Daha önce ziyaret edilen durumları saklamak için bir küme
    yigin = []  # DFS'de kullanılacak olan yığın yapısı
    ebeveyn_haritasi = {}  # Her durumun önceki durumunu saklayarak çözüm yolu oluşturmak için

    baslangic = (0, 0)  # Başlangıç durumu: (0, 0) yani her iki şişe de boş
    yigin.append(baslangic)  # Başlangıç durumunu yığına ekle
    ziyaret_edilenler.add(baslangic)  # Başlangıç durumunu ziyaret edilmiş olarak işaretle
    ebeveyn_haritasi[baslangic] = None  # Başlangıç durumunun ebeveyni yok

    print("\n[DFS Arama Ağacı]")

    while yigin:
        mevcut = yigin.pop()  # Yığının başından bir durum al
        a, b = mevcut

        print(f"Mevcut Durum: {mevcut}")  # Mevcut durumu ekrana yazdır

        # Hedefe ulaşıldıysa, yolu geri izleyerek oluştur
        if a == hedef or b == hedef:
            yol = []  # Hedefe ulaşmak için yol listesi
            while mevcut is not None:
                yol.append(mevcut)  # Yolu oluştur
                mevcut = ebeveyn_haritasi[mevcut]  # Önceki durumu al
            return yol[::-1]  # Yolu ters çevirerek başlangıçtan sona doğru getir

        # Olası tüm sonraki durumları dene
        sonraki_durumlar = [
            (a_kapasite, b),  # A şişesini doldur
            (a, b_kapasite),  # B şişesini doldur
            (0, b),           # A şişesini boşalt
            (a, 0),           # B şişesini boşalt
            (a - min(a, b_kapasite - b), b + min(a, b_kapasite - b)),  # A'dan B'ye dök
            (a + min(b, a_kapasite - a), b - min(b, a_kapasite - a))   # B'den A'ya dök
        ]

        for durum in sonraki_durumlar:
            if durum not in ziyaret_edilenler:
                ziyaret_edilenler.add(durum)  # Durumu ziyaret et
                ebeveyn_haritasi[durum] = mevcut  # Ebeveyn haritasına ekle
                yigin.append(durum)  # Durumu yığına ekle

    return None  # Hedefe ulaşmak mümkün değilse None döndür

# Senaryoların tanımı
senaryolar = [
    {'A': 4, 'B': 3, 'hedef': 2},
    {'A': 5, 'B': 2, 'hedef': 1},
    {'A': 6, 'B': 4, 'hedef': 2}
]

# Her bir senaryo için çözüm süreci
for i, senaryo in enumerate(senaryolar, 1):
    A = senaryo['A']
    B = senaryo['B']
    hedef = senaryo['hedef']
    print(f"\n=== Senaryo {i} ===")
    print(f"A kapasite: {A}, B kapasite: {B}, Hedef: {hedef}")

    # Hedef, A ve B'nin EBOB'u ile bölünebilir mi?
    if hedef % ebob(A, B) != 0:
        print("Bu hedef hacim bu şişe kombinasyonu ile mümkün değil (EBOB kontrolü).")
        continue

       # BFS algoritmasını kullanarak çözüm yolunu bulma
    bfs_yolu = bfs_agaci(A, B, hedef)  # BFS algoritması ile çözüm yolunu hesapla
    dfs_yolu = dfs_agaci(A, B, hedef)  # DFS algoritması ile çözüm yolunu hesapla

    # Eğer BFS çözüm bulabilirse
    if bfs_yolu:
        print("\nBFS ile Bulunan Çözüm Yolu:")  # BFS ile bulunan çözüm yolunu yazdır
        for adim in bfs_yolu:  # BFS yolunda her bir adımı yazdır
            print(adim)  # Adımı ekrana yazdır
        print(f"Toplam adım sayısı: {len(bfs_yolu) - 1}")  # Toplam adım sayısını yazdır
    else:
        print("\nBFS ile çözüm bulunamadı.")  # BFS ile çözüm bulunamadığında mesaj yazdır

    # Eğer DFS çözüm bulabilirse
    if dfs_yolu:
        print("\nDFS ile Bulunan Çözüm Yolu:")  # DFS ile bulunan çözüm yolunu yazdır
        for adim in dfs_yolu:  # DFS yolunda her bir adımı yazdır
            print(adim)  # Adımı ekrana yazdır
        print(f"Toplam adım sayısı: {len(dfs_yolu) - 1}")  # Toplam adım sayısını yazdır
    else:
        print("\nDFS ile çözüm bulunamadı.")  # DFS ile çözüm bulunamadığında mesaj yazdır

