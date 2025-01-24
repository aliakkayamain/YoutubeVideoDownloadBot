# **YouTube Video Downloader**

Bu proje, kullanıcıların YouTube videolarını farklı kalite seçenekleriyle indirmelerini sağlayan bir web uygulamasıdır. Flask kullanılarak geliştirilmiş, modern bir arayüz için Bootstrap kullanılmıştır.

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

🎯 Özellikler
	•	YouTube Video İndirici: Kullanıcıların YouTube videolarını farklı kalite seçenekleriyle indirmelerini sağlar.
	•	Tema Desteği: Açık ve karanlık mod arasında kolayca geçiş yapılabilir.
	•	İndirilen Videoların Listelenmesi: İndirilen videolar listelenir ve kullanıcıya sunulur.
	•	Kolay Kurulum: requirements.txt sayesinde bağımlılıklar hızlıca yüklenebilir.

🚀 Kurulum ve Çalıştırma

Gerekli Bağımlılıkların Yüklenmesi

	1.	Projeyi klonlayın:
	git clone https://github.com/kullaniciAdi/YoutubeVideoDownloadBot.git
	cd YoutubeVideoDownloadBot

	2.	Sanal ortam oluşturun ve etkinleştirin:
	python3 -m venv venv
	source venv/bin/activate  # Windows için: venv\Scripts\activate

	3.	Gereken Python kütüphanelerini yükleyin:
	pip install -r requirements.txt


Uygulamayı Çalıştırma

	1.	İndirilen videolar için bir klasör oluşturun:
	mkdir videoSavingfolder

	2.	Uygulamayı başlatın:
	python run.py

	3.	Tarayıcınızı açın ve şu adrese gidin:
	http://127.0.0.1:5000

📘 Kullanım

	1.	Video URL’sini Girin: İndirmek istediğiniz YouTube video URL’sini forma yazın.
	2.	Video Kalitesini Seçin: Kalite seçeneklerinden birini seçin (ör. 1080p, 720p).
	3.	“İndir” Butonuna Tıklayın: Video seçilen kalitede indirilecektir.
	4.	İndirilen Videoları Görüntüleyin: İndirilen videolar liste halinde gösterilir.

🛠️ Geliştirme Notları

	•	Tema Değişimi: scripts.js dosyasındaki tema değişim fonksiyonları güncellenebilir.
	•	Yeni Özellikler: Başka platformlardan indirme özelliği eklenebilir veya daha fazla kalite seçeneği eklenebilir.
	•	Config Güncellemeleri: settings/config.py dosyasını düzenleyerek indirilen videoların varsayılan kaydedileceği klasörü değiştirebilirsiniz.

🔑 Önemli Notlar

	•	run.py ile çalıştırılır: Proje başlatma işlemleri bu dosyada tanımlıdır.
	•	Git’e dahil edilmeyen dosyalar: .gitignore dosyasında, venv/, __pycache__/ gibi gereksiz dosyalar hariç tutulmuştur.

📬 İletişim

Sorularınız veya geri bildirimleriniz için bana ulaşabilirsiniz:
📧 aliakkayamain@gmail.com

.
