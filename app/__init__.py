import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    app = Flask(
        __name__,
        template_folder="../app/templates",  # Şablonlar için doğru yol
        static_folder="../app/static"       # Statik dosyalar için doğru yol
    )
    # .env dosyasını yükle
    load_dotenv()

    # Secret Key'i tanımla
    app.secret_key = os.getenv("SECRET_KEY", "default-secret-key")  # Çevresel değişken yoksa varsayılanı kullan

    # Blueprint'i kaydet
    from app.routes import main
    app.register_blueprint(main)
    
    return app