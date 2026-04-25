---
title: "Log Pengembang Kana Juku (Bagian 1): Dari Chatbots hingga Agen AI"
date: 2026-02-22T13:16:34.278Z
author: "QQder"
categories:
  - Lokakarya
tags:
  - Aplikasi iOS
  - AI di Perangkat
  - Pengenalan Tulisan Tangan
  - udemy
  - claude
  - kode claude
  - Gemini
  - gemini cli
  - UI cepat
  - UIKit
keywords:
  - Agen AI
  - kode claude
  - gemini cli
  - pengembangan iOS
  - pengembang indie
  - kana juku
  - pembelajaran bahasa Jepang
  - UI cepat
  - AI di Perangkat
  - karya
  - chatbot
description: "Berbagi pengalaman saya mengembangkan aplikasi pertama saya, Kana Juku — sebuah perjalanan yang juga menelusuri peralihan saya dari chatbots ke agen AI"
---


# Kata pengantar

Kana Juku adalah aplikasi pertama yang saya buat dan kirimkan ke App Store.

Karena ini adalah cerita pertama saya, ada cerita lengkap yang bisa dibagikan.

Seri ini mencakup proses pengembangan, cara saya menggunakan bantuan AI dan perkembangannya, bekerja dengan kumpulan data publik dan pertimbangan hak cipta, dan banyak lagi.

Jika aplikasi lain memiliki cerita penting, saya akan mempublikasikannya secara terpisah.

Postingan ini berfokus pada transisi dari chatbots ke agen AI yang dimulai pada **Q4 2025**.

Segalanya bergerak cepat di ruang ini, jadi saya secara blak-blakan mencatat waktu pada momen-momen penting.

## Tentang Aplikasi

Jika Anda memiliki perangkat Apple, silakan unduh dan cobalah.

Beberapa postingan mendatang juga akan menggunakan aplikasi ini sebagai contoh berjalan — topik seperti membersihkan [kumpulan data ETL](https://etlcdb.db.aist.go.jp/), [Apple Create ML](https://developer.apple.com/machine-learning/create-ml/), [PyTorch](https://pytorch.org/), [VOICEVOX](https://voicevox.hiroshiba.jp/), model bahasa besar di perangkat, dan banyak lagi.

Kana Juku: [URL](https://apps.apple.com/us/app/%E5%81%87%E5%90%8D%E7%A7%81%E5%A1%BE/id6756785942)

![](/images/IMG_2433.JPG)

***

# Garis Waktu Pengembangan

### Motivasi

Saya dan keluarga sama-sama tertarik untuk belajar bahasa Jepang, dan saya sudah lama menginginkan aplikasi pembelajaran bahasa Jepang yang sesuai dengan kebutuhan kami.

Masalah keluarga saya adalah mereka tidak bisa membaca bahasa Inggris, jadi romaji di sebagian besar buku teks dan aplikasi tidak ada artinya bagi mereka.

Bagi saya, saya sangat ingin kana ditampilkan di samping asal kanjinya (misalnya, "あ" berasal dari "安").

Gangguan lainnya: Saya memasang keyboard Jepang untuk penggunaan sesekali, namun mengganti metode input setiap hari berarti ketukan ekstra untuk melewati keyboard Jepang — sedikit gesekan yang bertambah.

### Persiapan Awal

**[Q4 2024]**

Saya sedang berada di antara pekerjaan pada saat itu, jadi saya memiliki bandwidth untuk mengambil kursus [Udemy](https://www.udemy.com/). Karena saya memiliki pengalaman JavaScript, saya mulai dengan [React](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih6Kzo2O-SAxUl3zQHHZoSL-kQFnoECDYQAQ&url=https%3A%2F%2Fzh-hant.legacy.reactjs.org%2F&usg=AOvVaw3Q6fqYyboB_gQOnPVX_tbN&opi=89978449) & [Expo](https://expo.dev/).

Pada tahap ini saya mengikuti konten kursus — halaman bergaya web sederhana, ditambah tambahan seperti GPS, kontrol kamera, dan pengambilan data jarak jauh.

Namun karena ini bukan ekosistem asli Apple, ada banyak alat tambahan yang harus dikelola.

**[Q1 2025]**

Setelah ragu-ragu untuk waktu yang lama, saya membeli Mac Mini dan beralih sepenuhnya ke SwiftUI milik Apple. Sekali lagi, saya belajar dari kursus Udemy.

Sebagian besar waktu saya digunakan untuk membiasakan diri dengan komponen dan tata letak UI dasar, ditambah semua fitur dasar — ​​persistensi data, pengambilan data, penyematan peta — dan yang setara dengan SwiftUI.

SwiftUI lebih modern dan tidak digabungkan dengan Xcode seperti UIKit, tetapi juga lebih sulit untuk memprediksi bagaimana sebenarnya tampilan tata letak SwiftUI. Awalnya saya terlalu memedulikan hal itu dan menghabiskan banyak waktu untuk bereksperimen.

**[Q3 2025]**

Karena saya memiliki pekerjaan harian dan hanya dapat membuat kode di malam hari — dan tidak setiap malam — kemajuannya lambat. Saya pada dasarnya membangun kerangka dasar dan memasukkan data bahasa Jepang.

Dengan aplikasi pertama, sulit memperkirakan bentuk akhirnya, jadi saya terus merevisinya. Kadang-kadang saya kembali untuk menonton ulang video kursus untuk mengetahui fitur-fitur yang sekarang saya tahu saya perlukan. Intinya, saya membayar uang sekolah.

Hingga saat ini, mulai **Q1 2024**, chatbot biasa seperti ChatGPT sudah sangat membantu dalam coding.

Namun siklus salin-tempel dan penjelasan konteks yang sangat banyak sangat memakan waktu. Outputnya sering kali meleset pada percobaan pertama atau keluar jalur, membuat saya kembali ke loop salin-tempel. Ini tidak pernah mencapai siklus umpan balik positif – hanya berguna sebagai referensi pembelajaran.

Pada saat itu, alat paling populer sebenarnya adalah editor Kursor dengan pelengkapan otomatis tabnya, tetapi memerlukan langganan untuk penggunaan yang berarti, jadi saya **tidak mencobanya**.

Sementara itu, Claude sudah mendapatkan popularitas sebagai model pengkodean terbaik, dan Anthropic telah merilis Claude Code — agen AI yang berjalan di mesin lokal Anda. Tapi sekali lagi, ini memerlukan langganan, jadi saya tidak mencobanya.

***

### Beralih ke Agen AI

**[Q4 2025]**

Pada titik ini saya berharap saya hanya akan berlangganan satu chatbot dalam satu waktu, dan saya baru saja beralih dari ChatGPT ke Google Gemini.

Spec-Driven Development (SDD) sedang menjadi tren, dan Google telah meluncurkan Gemini CLI — jawaban mereka terhadap Claude Code — jadi saya akhirnya **mencobanya**.

Saya menemukan bahwa agen menghilangkan langkah salin-tempel sepenuhnya, sehingga meningkatkan efisiensi secara besar-besaran. Langkah menempelkan kembali kode dan mencari baris mana yang akan diubah juga hilang.

Saat itu saya yakin: untuk coding, Anda harus menggunakan agen, bukan chatbot. Jadi saya langsung berlangganan Claude untuk menggunakan Kode Claude (CC mulai sekarang).

Model yang mendasari CC jelas lebih kuat. Pemahamannya terhadap percakapan dan kemampuannya untuk melaksanakan seperti yang diharapkan sudah sangat dapat diandalkan.

#### Mengontrol Komputer, dan Opus 4.5

Suatu saat disk Mac Mini saya penuh dan mesin tidak dapat digunakan. Saya baru saja bertanya kepada CC apa yang harus dilakukan — sama seperti saya mengajukan pertanyaan di halaman web chatbot.

CC kembali dengan rencana konkrit: direktori mana yang dapat dibersihkan, direktori mana yang dapat dipindahkan ke drive eksternal, dan seterusnya.

Saya khawatir hal ini akan merusak komputer saya, jadi saya menyetujui setiap langkah satu per satu. Pada akhirnya, semuanya berjalan lancar.

Saya tidak terlalu paham dengan macOS atau lingkungan build Xcode. Saat itulah saya menyadari bahwa AI memiliki setidaknya 80% pemahaman tentang *segala sesuatu* — termasuk hal-hal yang tidak saya ketahui — dan bahwa kemampuan menulis kode kira-kira setara dengan kemampuan mengoperasikan komputer.

Karena CC dapat mengontrol mesin secara langsung, CC dapat berpindah dengan bebas antar direktori, menulis kode, melihat kesalahannya sendiri, dan memperbaikinya — sebuah putaran umpan balik positif yang sepenuhnya mandiri.

Kecepatan pengembangan agen berada pada level yang sangat berbeda, dan fakta bahwa saya telah menunggu tiga bulan ekstra sebelum beralih ke CC membuat saya merasa sangat bodoh.

Waktu yang terbuang sangatlah mengejutkan, baik secara subyektif maupun obyektif.

Secara subyektif: jika saya mengadopsi alat-alat terbaru lebih awal, pekerjaan tiga bulan sebelumnya dapat diselesaikan dalam dua hingga tiga minggu.

Secara obyektif: orang lain yang menggunakan alat terbaru lebih produktif daripada saya dan mengirimkan produknya lebih cepat.

Penolakan saya sebelumnya untuk mencoba — mungkin menghemat waktu penyiapan setengah jam dan biaya berlangganan beberapa ratus dolar — akhirnya menyia-nyiakan sebagian besar hidup saya.

Ini mungkin juga menjelaskan mengapa begitu banyak orang terobsesi mengejar berita produk AI terkini.

Setidaknya begitulah yang terjadi pada saya — saya tidak bisa tidak mengikuti perkembangan rilisan terbaru. Ini adalah bentuk lindung nilai risiko manajemen waktu.

**[24 November 2025]**

Opus 4.5 dirilis. Opus adalah model andalan tingkat tertinggi Claude, dan versi 4.5 baru saja dirilis.

Selain peningkatan kinerja yang signifikan dibandingkan pendahulunya, perbedaan terbesarnya adalah pemahaman tentang maksudnya.

Versi lama pada dasarnya melakukan persis seperti yang Anda tunjukkan (yang sejujurnya sudah cukup bagus). Dimulai dengan 4.5, setelah menerima permintaan Anda, pertama-tama akan diringkas dan direncanakan sampai tingkat tertentu. Dalam istilah manusia: ia menjadi lebih tajam, lebih berpengalaman.

Anda tidak perlu lagi menjelaskan file mana yang akan diubah dan bagaimana caranya. Anda dapat mendeskripsikan tujuan akhir seperti seorang manajer atau eksekutif, dan tujuan tersebut akan diuraikan dan merencanakan beberapa langkah berikutnya sendiri.

Kemampuan perencanaan ini semakin meningkatkan efisiensi. Seperti yang saya sebutkan, AI sudah mengetahui setidaknya 80% dari segalanya — sekarang AI secara proaktif melakukan langkah kerja selanjutnya, dan melakukannya dengan baik.

Dikombinasikan dengan ini, saya dapat beroperasi pada tingkat abstraksi yang jauh lebih tinggi. Semakin banyak yang didelegasikan ke CC. Lambat laun, saya tidak lagi perlu membaca atau mengedit kode sendiri.

Setelah Opus 4.5 keluar, perdebatan di media sosial tentang apakah AI dapat menulis kode pada dasarnya berakhir.

Untuk insinyur perangkat lunak penuh waktu dan profesional berpengalaman, saya tidak dapat menceritakan pengalaman mereka.

Namun dibandingkan dengan diri saya sendiri: hal-hal yang memakan waktu satu hingga dua tahun kini dapat diselesaikan dalam dua hingga tiga bulan.

Outputnya berada di luar batas pengetahuan saya - saya sebenarnya adalah hambatan terbesar.

*Akhir Bagian 1*
