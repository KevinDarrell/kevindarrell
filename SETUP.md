# 🚀 Cara Publish Profile README

Repo ini sudah di-`git init` dan semua file (termasuk `.github/` dan `assets/`)
sudah ke-commit. Kamu tinggal push. Ada 2 cara:

---

## Opsi A — Push via Terminal (paling cepat, direkomendasikan)

1. Buat repo KOSONG di GitHub: https://github.com/new
   - **Repository name** harus PERSIS username kamu: `KevinDarrell`
   - Set **Public**
   - JANGAN centang "Add a README" / .gitignore / license (biarkan kosong)
   - Create repository

2. Di folder ini, jalankan (ganti URL kalau pakai SSH):
   ```bash
   git remote add origin https://github.com/KevinDarrell/KevinDarrell.git
   git branch -M main
   git push -u origin main
   ```

Selesai. Buka https://github.com/KevinDarrell 🎉

---

## Opsi B — Upload manual (tanpa terminal)

1. Buat repo `KevinDarrell` (Public) + centang "Add a README file".
2. **Add file → Upload files** → drag `README.md`.
3. Bikin file `assets/header.svg` → **Add file → Create new file**, ketik
   `assets/header.svg`, paste isinya, commit.
4. Bikin `.github/workflows/snake.yml` dengan cara yang sama.

---

## Aktifkan Snake Animation 🐍  (WAJIB biar snake muncul)

Snake butuh GitHub Actions yang jalan sekali dulu:

1. Di repo → tab **Actions**. Kalau ada tombol enable workflows, klik.
2. Pilih **"Generate Snake Animation"** → **Run workflow**.
3. Tunggu ±1 menit (centang hijau ✅). Ini bikin branch `output`.
4. Refresh profil — snake monochrome langsung muncul. Update otomatis tiap hari.

> Gagal soal permission? Buka **Settings → Actions → General →
> Workflow permissions** → pilih **Read and write permissions** → Save →
> jalankan ulang workflow-nya.

---

## ✏️ 2 hal yang WAJIB kamu edit

1. **LinkedIn** — di `README.md` bagian `▸ CONNECT`, ganti `YOUR-LINKEDIN`
   dengan handle-mu. Contoh: URL `linkedin.com/in/kevin-darrell` → tulis `kevin-darrell`.
2. **STACK** — sesuaikan badge dengan tools yang benar-benar kamu kuasai.
   Tambah/hapus badge tinggal copy satu baris. Nama logo: https://simpleicons.org

---

## Mau ganti isi header (nama/tagline/chip)?

Edit `assets/header.svg` — teksnya jelas kok: cari `KEVIN DARRELL`,
`SOFTWARE ENGINEER`, `I build systems that think`, dan chip `SYSTEMS/BACKEND/SCALE`.
