from locust import HttpUser, task, between
import random 
class HepsiburadaMusterisi(HttpUser):
    # Kullanıcılar işlem arası 1-5 saniye beklesin
    wait_time = between(1, 5)
    # Test verilerimiz
    aranacak_urunler = ["iphone 15", "samsung s24", "nike ayakkabi", "bebek bezi", "airfryer", "laptop"]
    # --- 1. YAŞAM DÖNGÜSÜ (Login Simülasyonu) ---
    def on_start(self):
        print("👤 Yeni bir kullanıcı siteye giriş yaptı!")
    # --- 2. AKILLI ARAMA (Vitrin & Arama) ---
    @task(3)
    def urun_ara(self):
        # Listeden rastgele ürün seç
        secilen_urun = random.choice(self.aranacak_urunler)
        #Cache etkisini azaltmak için
        # Dinamik URL oluştur ve Performans Kontrolü yap
        with self.client.get(f"/ara?q={secilen_urun}", catch_response=True) as response:
            # Veriyi URL'in ucuna ekliyoruz (/ara?q=iphone). JSON paketi yok
            # Burada GET isteği yapıyoruz çünkü veri kaynağımız yukarıda aranacak_urunler, eğer yoktan var etmek isteseydik
            # POST kullanmamız gerekirdi.
            if response.elapsed.total_seconds() > 0.5:
                response.failure(f"Çok yavaş! {secilen_urun} araması 0.5 saniyeden uzun sürdü.")
    # --- 3. SEPETE EKLEME (Darboğaz Testi) ---
    @task(1)
    def sepete_ekle(self):
        # Rastgele ID üret
        urun_id = random.randint(1000, 9999)
        self.client.post("/sepetime/ekle", json={
            "urun_id": urun_id,
            "adet": 1,
            "satici": "Hepsiburada"
        })
        # Sen bu kodu çalıştırdığında, Hepsiburada'nın sunucusuna (sanal olarak) gidip;
        #  "Merhaba, ben 4521 numaralı üründen 1 tane almak istiyorum, işte formu" diyorsun.
        # Sunucu da bu formu alıyor ve veritabanına YAZMAYA (Create) çalışıyor. İşte bu yüzden adı POST (Gönder/Yarat) isteği.

    # --- 4. KAMPANYA SAYFASI ---
    @task(2)
    def kampanya_sayfasi(self):
        self.client.get("/efsane-cuma-indirimleri")