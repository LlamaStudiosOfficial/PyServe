import sys
import os
import json
import random
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, jsonify

if getattr(sys, 'frozen', False):
    # Running as .exe
    base_path = sys._MEIPASS
else:
    # Running from source
    base_path = os.path.abspath(".")

template_folder = os.path.join(base_path, "templates")
static_folder = os.path.join(base_path, "static")


app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


ASSET_FOLDER = "assets"
META_FILE = os.path.join(ASSET_FOLDER, "meta.json")

os.makedirs(ASSET_FOLDER, exist_ok=True)


def rot19(s: str) -> str:
    out = []
    for c in s:
        if "a" <= c <= "z":
            out.append(chr((ord(c) - 97 + 19) % 26 + 97))
        elif "A" <= c <= "Z":
            out.append(chr((ord(c) - 65 + 19) % 26 + 65))
        else:
            out.append(c)
    return "".join(out)


def save_meta(data):
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_meta():
    if not os.path.exists(META_FILE):
        save_meta({})
        return {}
    try:
        with open(META_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except json.JSONDecodeError:
        save_meta({})
        return {}


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/server")
def server():
    files = [f for f in os.listdir(ASSET_FOLDER) if f != "meta.json"]
    meta = load_meta()

    file_info = []
    for f in files:
        path = os.path.join(ASSET_FOLDER, f)
        size = os.path.getsize(path)
        m = meta.get(f, {})
        public_meta = {
            "uploader": m.get("uploader"),
            "ip": m.get("ip"),
        }
        file_info.append({
            "name": f,
            "size": size,
            "meta": public_meta,
        })

    pw = request.args.get("pw")
    return render_template("server.html", title="Server", files=file_info, pw=pw)


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    device_id = request.form.get("device_id") or "unknown-xxxxxx.hidden"
    if not file or file.filename == "":
        return redirect(url_for("server"))

    filename = file.filename
    file.save(os.path.join(ASSET_FOLDER, filename))

    password = rot19(device_id) + str(random.randint(1, 256))

    meta = load_meta()
    meta[filename] = {
        "uploader": device_id,
        "ip": request.remote_addr,
        "password": password,
    }
    save_meta(meta)

    return redirect(url_for("server", pw=password))


@app.route("/delete/<filename>", methods=["POST"])
def delete_file(filename):
    meta = load_meta()
    stored = meta.get(filename, {})
    submitted_pw = request.form.get("password", "")

    if not stored or stored.get("password") != submitted_pw:
        return redirect(url_for("server"))

    path = os.path.join(ASSET_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)

    if filename in meta:
        del meta[filename]
        save_meta(meta)

    return redirect(url_for("server"))


@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(ASSET_FOLDER, filename, as_attachment=True)


@app.route("/filelist")
def filelist():
    files = [f for f in os.listdir(ASSET_FOLDER) if f != "meta.json"]
    meta = load_meta()

    file_info = []
    for f in files:
        path = os.path.join(ASSET_FOLDER, f)
        size = os.path.getsize(path)
        m = meta.get(f, {})
        public_meta = {
            "uploader": m.get("uploader"),
            "ip": m.get("ip"),
        }
        file_info.append({
            "name": f,
            "size": size,
            "meta": public_meta,
        })

    return jsonify(file_info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
