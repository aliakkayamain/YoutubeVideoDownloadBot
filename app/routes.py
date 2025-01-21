from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
import os
from app.services import download_videos
from settings.config import DOWNLOAD_FOLDER

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        quality = request.form.get("quality", "best")

        if not url:
            flash("Lütfen bir URL giriniz!", "error")
            return redirect(url_for("main.index"))

        try:
            download_videos([url], DOWNLOAD_FOLDER, quality)
            flash("Video başarıyla indirildi!", "success")
        except Exception as e:
            flash(f"Video indirme hatası: {str(e)}", "error")

        return redirect(url_for("main.index"))

    # İndirilen dosyaların listesi
    videos = os.listdir(DOWNLOAD_FOLDER)
    return render_template("index.html", videos=videos)

@main.route("/download/<filename>")
def download_file(filename):
    """ İndirilen dosyaları kullanıcıya sunar. """
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)