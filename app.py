import json
import sys
from pathlib import Path

from flask import Flask, jsonify, render_template_string

BASE_DIR = Path(__file__).parent
app = Flask(__name__)

INDEX_HTML = """<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Waspada Digital</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 640px; margin: 0 auto; padding: 16px; line-height: 1.5; }
    .case { border: 1px solid #ccc; border-radius: 8px; padding: 12px; margin: 12px 0; }
    .msg { background: #f4f4f4; padding: 8px; border-radius: 6px; white-space: pre-wrap; }
    summary { cursor: pointer; font-weight: 600; margin-top: 8px; }
  </style>
</head>
<body>
  <h1>Waspada Digital</h1>
  <p>Latihan mengenali hoaks dan pesan penipuan (phishing). Baca setiap pesan,
     tebak apakah pesan itu valid, hoaks, atau phishing, lalu buka jawabannya.
     Semua contoh bersifat fiktif.</p>
  {% for c in cases %}
  <div class="case">
    <strong>{{ c.id }}. {{ c.judul }}</strong>
    <div class="msg">{{ c.isi_pesan }}</div>
    <details>
      <summary>Lihat jawaban</summary>
      <p>Jenis: <strong>{{ c.jenis }}</strong></p>
      <p>{{ c.penjelasan }}</p>
    </details>
  </div>
  {% endfor %}
</body>
</html>"""


def load_cases():
    with open(BASE_DIR / "cases.json", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    return render_template_string(INDEX_HTML, cases=load_cases())


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/api/info")
def info():
    return jsonify(
        app="waspada-digital",
        module="M03",
        version="0.1.0",
        python=sys.version.split()[0],
        total_cases=len(load_cases()),
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
