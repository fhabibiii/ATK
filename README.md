# Analisis Tingkat Kebisingan

Program ini dibuat untuk memenuhi tugas mata kuliah **Internet of Things (IoT) dengan Kemampuan Cerdas**. Program ini bertujuan untuk menganalisis tingkat kebisingan berdasarkan data dari file Excel, kemudian mengkategorikan hasil analisis tersebut.

## Fitur Utama
- **Memuat File Excel**: Program dapat memuat file Excel berisi data amplitudo suara.
- **Menghitung Rata-Rata Kebisingan**: Menghitung nilai rata-rata tingkat kebisingan berdasarkan kolom `Sound pressure level (dB)` dari baris tertentu.
- **Kategorisasi Tingkat Kebisingan**: Memberikan hasil analisis berupa kategori tingkat kebisingan dengan deskripsi dampaknya.

## Teknologi yang Digunakan
- **Kivy**: Framework Python untuk membuat antarmuka pengguna.
- **Pandas**: Library Python untuk manipulasi dan analisis data.

## Instalasi
1. Pastikan Python 3.7 atau versi lebih baru telah diinstal.
2. Instal dependensi yang diperlukan:
   ```bash
   pip install kivy pandas openpyxl
   ```

## Cara Menjalankan Program
1. Simpan kode dalam file `Analisis Tingkat Kebisingan.py`.
2. Jalankan program menggunakan perintah:
   ```bash
   python Analisis Tingkat Kebisingan.py
   ```
3. Pilih file Excel yang berisi data kebisingan. File harus memiliki:
   - Nama sheet: `Amplitudes`
   - Kolom: `Sound pressure level (dB)`
4. Program akan menghitung rata-rata tingkat kebisingan dan menampilkan hasil dalam popup.

## Struktur File Excel
Program mengasumsikan struktur berikut pada file Excel:
- **Nama sheet**: `Amplitudes`
- **Kolom data**: `Sound pressure level (dB)`
- **Baris mulai**: Baris ke-4 (indeks 3)

## Kategori Tingkat Kebisingan
1. **< 30 dB**: Suara yang tenang, dapat membantu relaksasi dan mengurangi stres.
2. **31 - 50 dB**: Kebisingan sedang, dapat mengganggu konsentrasi saat bekerja atau belajar.
3. **51 - 70 dB**: Kebisingan tinggi, dapat mengganggu tidur, menyebabkan stres.
4. **71 - 90 dB**: Kebisingan sangat tinggi, dapat merusak pendengaran dan menyebabkan tuli permanen.
5. **> 90 dB**: Tidak Dikategorikan.

## Catatan Penting
- Pastikan file Excel memiliki format dan struktur yang sesuai dengan deskripsi di atas.
- Program hanya mendukung file Excel dengan ekstensi `.xlsx`.

## Kontributor
- Nama: Faqihuddin Habibi
- Mata Kuliah: IoT dengan Kemampuan Cerdas

## Lisensi
Program ini dilisensikan di bawah [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang program ini selama mengikuti ketentuan lisensi.