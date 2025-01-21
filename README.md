# YouTube Video Downloader

Bu proje, kullanıcıların YouTube videolarını istedikleri kalite düzeyinde indirmelerini sağlayan bir web uygulamasıdır. Flask tabanlı olarak geliştirilmiştir ve Bootstrap kullanılarak modern bir kullanıcı arayüzü sunulmaktadır.

---

## Proje Hiyerarşisi

```plaintext
YOUTUBEVIDEODOWNLOADBOT/
├── app/
│   ├── __init__.py             # Flask uygulama yapılandırması
│   ├── routes.py               # Flask rotaları (HTTP endpoint'ler)
│   ├── services.py             # Video indirme ve iş mantığı
│   ├── templates/
│   │   └── index.html          # Uygulama arayüzü (HTML)
│   ├── static/
│   │   ├── css/
│   │   │   ├── base.css        # Temel CSS
│   │   │   ├── darkMode.css    # Karanlık mod için CSS
│   │   │   └── lightMode.css   # Açık mod için CSS
│   │   ├── images/
│   │   │   ├── youtube_logo.png # YouTube logosu
│   │   │   └── youtube.png      # Favicon
│   │   └── js/
│   │       └── scripts.js      # JavaScript dosyaları
├── settings/
│   ├── __init__.py             # Ayarlar modülü
│   └── config.py               # Konfigürasyon ayarları
├── venv/                       # Sanal ortam (Git'e dahil edilmez)
├── videoSavingfolder/          # İndirilen videoların saklandığı klasör
├── .gitignore                  # Git izlememesi gereken dosya ve klasörler
├── README.md                   # Projenin açıklaması ve kullanımı
├── requirements.txt            # Gereken Python kütüphaneleri
├── run.py                      # Uygulamanın başlatılması için ana dosya
└── videoLink.txt               # Toplu video indirme için video URL'leri

### Özellikler
	•	YouTube Video İndirici: Kullanıcıların YouTube videolarını farklı kalite seçenekleriyle indirmelerine olanak sağlar.
	•	Tema Desteği: Açık ve karanlık mod arasında geçiş yapılabilir.
	•	İndirilen Videoların Listelenmesi: İndirilen videolar kullanıcıya gösterilir ve yeniden indirilebilir.
	•	Kolay Kurulum: Sanal ortam ve bağımlılıkların kolay kurulumu için requirements.txt dosyası.

Kurulum ve Çalıştırma

Gerekli Bağımlılıkların Yüklenmesi
	1.	Bu projeyi klonlayın:
    git clone https://github.com/kullaniciAdi/youtubeVideoDownloadBot.git
    cd youtubeVideoDownloadBot

	2.	Sanal ortam oluşturun ve etkinleştirin:
    python3 -m venv venv
    source venv/bin/activate  # Windows için: venv\Scripts\activate

    3.	Gerekli Python kütüphanelerini yükleyin:
    pip install -r requirements.txt

Uygulamayı Çalıştırma
    1. videoSavingfolder klasörünün varlığını kontrol edin (eksikse oluşturulur):
    mkdir videoSavingfolder

    2.	Uygulamayı başlatın:
    python run.py

    3.	Tarayıcınızı açın ve şu adrese gidin:
    http://127.0.0.1:5000

Kullanım
	1.	Video URL’sini Girin: İndirmek istediğiniz YouTube video URL’sini forma yazın.
	2.	Video Kalitesini Seçin: Kalite seçeneklerinden birini seçin.
	3.	“İndir” Butonuna Tıklayın: Video seçilen kalitede indirilecektir.
	4.	İndirilen Videoları Görüntüleyin: İndirilen videolar uygulama arayüzünde listelenir.


Önemli Notlar
	•	Proje run.py dosyasıyla başlatılır.
	•	settings/config.py dosyasında indirme klasörü gibi ayarlar düzenlenebilir:

	•	Sanal ortam (venv) ve __pycache__ gibi gereksiz dosyalar .gitignore ile izlenmez.

Geliştirme Notları
	•	Tema Değişimi: scripts.js dosyasındaki tema değişim fonksiyonları güncellenebilir.
	•	Yeni Özellikler: Daha fazla kalite seçeneği veya başka platformlardan indirme özellikleri eklenebilir.

İletişim

Herhangi bir sorunuz varsa aliakkayamain@gmail.com adresinden iletişime geçebilirsiniz.