# Requirements

## Problem Statement

Siswa kelas X SMA mengalami kesulitan membedakan informasi valid dari

hoaks dan pesan penipuan (phishing) di media sosial dan aplikasi pesan.

Sistem menyediakan studi kasus dan latihan interaktif dengan umpan balik

otomatis sehingga kemampuan memverifikasi informasi dan mengenali

tanda-tanda phishing meningkat.

## Target Users

- Peserta latihan: Siswa kelas X SMA

- Fasilitator: guru penyusun studi kasus (fitur M05 ke atas)

## Functional Requirements

- FR-01 Sistem menampilkan halaman utama berisi tujuan dan petunjuk.

- FR-02 Sistem menyediakan endpoint /health.

- FR-03 Sistem menampilkan metadata aplikasi di /api/info.

- FR-04 Sistem menampilkan daftar studi kasus (data statis).

## Non-Functional Requirements

- NFR-01 Backend hanya listen pada loopback.

- NFR-02 Aplikasi dikelola systemd.

- NFR-03 Request publik masuk melalui reverse proxy.

- NFR-04 Secret tidak disimpan pada Git repository.

- NFR-05 Health endpoint mengembalikan HTTP 200 saat sehat.

- NFR-06 Deployment dapat direproduksi dari repository.

- NFR-07 Arsitektur sesuai VPS 2 vCPU / 1 GB RAM.

- NFR-08 Tidak ada pengumpulan data pribadi pada tahap awal.

- NFR-09 Contoh phishing memakai domain fiktif, bukan tautan aktif.

- NFR-10 Halaman nyaman dibaca di layar ponsel.

## Scope M03

In scope: repository, dokumentasi, aplikasi Flask dasar, SSH hardening,

Gunicorn, systemd, Caddy, UFW, deployment HTTP publik.

Out of scope: database, Docker, IaC, CI/CD, HTTPS/domain, scaling.

## Constraints

- Azure VM Standard B2ats v2: 2 vCPU, 1 GiB RAM (892 MiB terbaca), 30 GB disk

- Ubuntu Server 24.04 LTS

- IPv4 publik

## Acceptance Criteria M03

- [x] /health mengembalikan HTTP 200 dari klien eksternal

- [x] Backend hanya listen pada 127.0.0.1:8000

- [x] Aplikasi tetap berjalan setelah reboot

