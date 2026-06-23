# State Complexity Management

Repositori ini dibuat untuk keperluan praktikum mengenai **State Complexity Management** menggunakan bahasa Python. Praktikum ini membahas bagaimana state dalam program dapat menjadi sulit dikendalikan apabila tidak dirancang dengan jelas. Beberapa contoh dibuat dalam versi insecure untuk menunjukkan masalah yang dapat muncul, lalu dibandingkan dengan pendekatan yang lebih aman. Fokus utama project ini adalah memahami pengelolaan state, valid state, invalid state, dan transisi yang lebih terkontrol.

## Topik yang Dibahas

* Boolean Explosion
* State Machine
* Race Condition
* TOCTOU
* Atomic Transition
* Idempotency Key
* Snapshot
* Audit Trail
* Wallet Transfer Challenge

## Struktur File

```text
README.md
state-complexity-management/
├── 01_boolean_explosion_insecure.py
├── 02_order_state_machine_secure.py
├── 03_voucher_race_condition_insecure.py
├── 04_voucher_atomic_secure.py
├── 05_idempotency_key_demo.py
├── 06_snapshot_audit_trail.py
└── 07_wallet_transfer_challenge.py
```

## Penjelasan Singkat File

### 01_boolean_explosion_insecure.py

File ini menunjukkan masalah boolean explosion pada objek order. Banyak boolean digunakan untuk mewakili status seperti paid, shipped, delivered, cancelled, refunded, dan returned. Semakin banyak boolean yang dipakai, semakin banyak kombinasi state yang mungkin muncul. Beberapa kombinasi tersebut dapat menjadi invalid state yang seharusnya tidak terjadi.

### 02_order_state_machine_secure.py

File ini menunjukkan pendekatan yang lebih aman menggunakan state machine. Status order dibuat secara eksplisit menggunakan enum seperti CREATED, PAID, SHIPPED, dan DELIVERED. Perubahan status hanya boleh berjalan melalui urutan yang sudah ditentukan. Pendekatan ini membantu mencegah transisi state yang tidak valid.

### 03_voucher_race_condition_insecure.py

File ini menunjukkan race condition pada proses penggunaan voucher. Dua thread mencoba memakai voucher yang sama dalam waktu hampir bersamaan. Karena pengecekan dan perubahan state tidak dilakukan secara atomic, voucher dapat dipakai lebih dari satu kali. Contoh ini juga memperlihatkan masalah TOCTOU atau Time of Check to Time of Use.

### 04_voucher_atomic_secure.py

File ini memperbaiki masalah race condition dengan menggunakan Lock. Proses pengecekan dan perubahan status voucher dilakukan dalam satu blok yang tidak dapat dimasuki dua thread secara bersamaan. Dengan cara ini, hanya satu user yang dapat berhasil menggunakan voucher. Pendekatan ini menunjukkan pentingnya atomic transition pada operasi yang sensitif.

### 05_idempotency_key_demo.py

File ini menunjukkan penggunaan idempotency key pada payment callback. Callback pembayaran dapat terkirim lebih dari satu kali karena retry atau gangguan jaringan. Program menyimpan transaction id yang sudah diproses agar transaksi yang sama tidak diproses dua kali. Konsep ini penting untuk mencegah efek bisnis ganda seperti saldo bertambah dua kali.

### 06_snapshot_audit_trail.py

File ini menunjukkan penggunaan snapshot dan audit trail pada perubahan state pembayaran. Setiap perubahan state dicatat dengan informasi waktu, aktor, state lama, dan state baru. Program juga membatasi perpindahan state berdasarkan transisi yang diizinkan. Audit trail membantu proses pelacakan perubahan dan membuat sistem lebih mudah diaudit.

### 07_wallet_transfer_challenge.py

File ini merupakan challenge yang menunjukkan contoh transfer wallet yang masih insecure. Program memperlihatkan masalah seperti sender dan receiver yang sama, amount negatif, dan status yang dapat diubah bebas. Bagian ini menjadi latihan untuk membuat versi yang lebih aman menggunakan prinsip secure by design. Konsep yang relevan meliputi validasi data, state transition, dan pembatasan perubahan status.

## Cara Menjalankan

### 1. Cek Apakah Python 3 Sudah Terpasang

Buka Terminal (Linux/macOS) atau Command Prompt/PowerShell (Windows), lalu jalankan:

```bash
python --version
```

atau

```bash
python3 --version
```

Jika Python 3 sudah terpasang, akan muncul output yang menampilkan versi Python yang terinstal, misalnya:

```text
Python 3.11.5
```

### 2. Jika Python Belum Terpasang

Unduh dan instal Python dari situs resmi:

https://www.python.org/downloads/

Khusus pengguna Windows, pastikan mencentang opsi:

```text
Add Python to PATH
```

saat proses instalasi.

### 3. Masuk ke Folder Project

Buka terminal lalu pindah ke folder project:

```bash
cd state-complexity-management
```

### 4. Jalankan Program

Jalankan file satu per satu melalui terminal:

```bash
python 01_boolean_explosion_insecure.py
python 02_order_state_machine_secure.py
python 03_voucher_race_condition_insecure.py
python 04_voucher_atomic_secure.py
python 05_idempotency_key_demo.py
python 06_snapshot_audit_trail.py
python 07_wallet_transfer_challenge.py
```

Jika perintah `python` tidak dikenali, gunakan:

```bash
python3 01_boolean_explosion_insecure.py
python3 02_order_state_machine_secure.py
python3 03_voucher_race_condition_insecure.py
python3 04_voucher_atomic_secure.py
python3 05_idempotency_key_demo.py
python3 06_snapshot_audit_trail.py
python3 07_wallet_transfer_challenge.py
```

### 5. Verifikasi Output

Setelah dijalankan, setiap file akan menampilkan output sesuai konsep yang sedang didemonstrasikan, seperti state machine, race condition, atomic transition, idempotency key, audit trail, dan wallet transfer challenge.

## Tujuan Praktikum

Praktikum ini bertujuan untuk memahami bagaimana state yang tidak dikelola dengan baik dapat menghasilkan kondisi yang salah atau tidak aman. Melalui beberapa contoh program, project ini menunjukkan perbedaan antara state yang dibiarkan bebas dan state yang dikelola dengan aturan transisi yang jelas. Praktikum ini juga membantu memahami race condition, atomic operation, idempotency, dan audit trail secara sederhana. Materi ini relevan untuk sistem yang memiliki proses status seperti order, voucher, pembayaran, dan transfer saldo.

## Catatan Penting

Beberapa file pada repositori ini sengaja dibuat insecure untuk tujuan pembelajaran. Contoh insecure digunakan untuk menunjukkan masalah yang dapat muncul dalam pengelolaan state. Kode ini bukan implementasi siap production dan tidak ditujukan untuk digunakan langsung pada sistem nyata. Untuk penggunaan nyata, diperlukan validasi tambahan, penyimpanan permanen, pengamanan concurrency yang lebih kuat, serta desain state transition yang lebih lengkap.

## Disclaimer

Repositori ini merupakan demo praktikum sederhana untuk memahami konsep State Complexity Management. Implementasi di dalamnya dibuat agar mudah dipahami dan dijalankan secara lokal. Project ini lebih berfokus pada pembelajaran konsep dibandingkan implementasi production-ready. Pengembangan lebih lanjut diperlukan apabila konsep ini ingin diterapkan pada sistem nyata.
