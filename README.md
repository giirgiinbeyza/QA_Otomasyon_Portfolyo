[![Hepsiburada Otomasyon Robotu 🤖](https://github.com/giirgiinbeyza/QA_Otomasyon_Portfolyo/actions/workflows/test_robotu.yml/badge.svg)](https://github.com/giirgiinbeyza/QA_Otomasyon_Portfolyo/actions/workflows/test_robotu.yml)

# Hepsiburada Black Friday Load Test Simulation 🦗

## Proje Özeti (Project Summary)
Bu proje, **Python** ve **Locust** kütüphanesi kullanılarak, yüksek trafikli e-ticaret sitelerinin (Hepsiburada, Trendyol vb.) "Efsane Cuma" (Black Friday) dönemindeki kullanıcı davranışlarını simüle etmek amacıyla geliştirilmiştir.

## 🎯 Amaç (Goal)
Sistemin **ani yük (Spike Testing)** altındaki davranışını analiz etmek ve olası darboğazları (bottlenecks) tespit etmektir.

## 🛠 Kullanılan Teknolojiler (Tech Stack)
* **Dil:** Python 3.x
* **Araç:** Locust (Load Testing Framework)
* **IDE:** VS Code

## 🧪 Test Senaryosu (Scenario)
Kod, aşağıdaki kullanıcı davranışlarını ağırlıklandırılmış (Weighted Tasks) olarak simüle eder:
1.  **Ana Sayfa Ziyareti (%60):** Kullanıcıların çoğu sadece vitrine bakar.
2.  **Ürün Arama (%30):** Kullanıcılar belirli ürünleri (örn: iPhone 15) aratır.
3.  **Sepete Ekleme (%10):** En kritik ve sunucuyu en çok yoran işlemdir (POST Request).

## 🚀 Nasıl Çalıştırılır? (How to Run)
Terminal üzerinden aşağıdaki komut ile arayüz başlatılır:
```bash
locust -f main.py
