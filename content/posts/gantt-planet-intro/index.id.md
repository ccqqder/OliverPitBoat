---
title: "Gantt Planet: Ceruk dan Pertimbangan Pengembang Indie"
date: 2026-02-25T06:55:21.349Z
draft: false
categories:
  - Observatorium
tags:
  - Pengembang Indie
  - Toko Aplikasi
  - Bagan Gantt
  - Pengembangan Produk
  - Pengembangan dengan Bantuan AI
  - proyek sampingan
keywords:
  - pengembang indie
  - Toko Aplikasi
  - Bagan Gantt
  - Planet Gantt
  - pengembangan produk
  - proyek sampingan
  - Pengembangan yang dibantu AI
  - bagan Gantt kehidupan
  - visualisasi 3D
  - Aplikasi iOS
description: "App Store sebagai beranda pribadi era baru, menggunakan Gantt Planet sebagai studi kasus"
author: "QQder"
---


![](/images/gantt-planet-cover.jpg)

# Kata pengantar

Dalam postingan kali ini, saya akan membahas tentang pasar, sumber daya, ekosistem, dan proses pengembangan dari sudut pandang pengembang indie.
Sebagai plug-in yang tidak tahu malu, saya menggunakan Gantt Planet sebagai contoh saya: [URL](https://apps.apple.com/us/app/%E7%94%98%E7%89%B9%E6%98%9F%E7%90%83/id6757654373).
Saya akui sebelumnya bahwa ini hanyalah proyek sampingan saya – tekanannya sangat berbeda dengan seseorang yang mencari nafkah dari ini – jadi saya hanya membahas pendekatan penelitian di sini.

## Percikan dan Kios

Ide di balik Gantt Planet sederhana saja: alat bagan Gantt gratis — baik perangkat lunak desktop, aplikasi seluler, atau aplikasi web — semuanya sangat buruk untuk digunakan.
Yang tampaknya layak semuanya memerlukan biaya, jadi saya pikir saya akan membuat aplikasi bagan Gantt saya sendiri.

Tidak butuh waktu lama sebelum saya menyadari bahwa segala sesuatunya tidak sesederhana itu:

1. Melihat bagan Gantt bergaya spreadsheet di layar ponsel terlalu sempit
2. Bagan Gantt yang tepat perlu terhubung ke banyak sumber daya — email, kontak, ruang pertemuan, dan sebagainya

Menyelesaikan salah satu masalah ini memerlukan biaya yang mahal. Anda harus menghabiskan banyak waktu untuk menyempurnakan UI dan merancang alur penggunaan yang ideal, sambil menerima bahwa beberapa alur kerja tidak dapat diintegrasikan dan harus dihapus.

Mengenai integrasi sumber daya, Anda harus menangani proses masuk untuk semua platform utama, menangani API dan protokol autentikasi yang tak terhitung jumlahnya, dan mempertahankan semuanya di masa mendatang.

Pada titik ini, saya mengalami hambatan – dan ketika Anda bekerja pada skala yang tidak mendapatkan keuntungan dari skala ekonomi, hal tersebut tidak bisa dihindari.

## Putaran Setelah Putaran

Di momen seperti ini, saya suka mengambil masing-masing faktor dan memperluasnya satu atau dua langkah ke luar, mencari titik temu yang memungkinkan segala sesuatunya benar-benar berhasil.

Sebagai pengembang yang didorong oleh kepentingan pribadi, "layak" berarti biaya yang sangat rendah, ditambah proposisi nilai yang kecil namun jelas.

AI membantu saya mencapai bagian pertama — biaya yang sangat rendah.

Mengenai nilai, sebagian besar ditentukan sendiri, meskipun memantulkan ide dari AI juga dapat membantu mengkristalkan berbagai hal.

Bagi saya, hal ini terutama bertujuan untuk membangun sesuatu yang benar-benar ingin saya gunakan — setidaknya sesuatu yang ingin saya lihat. Selain itu, jika tidak ada orang lain yang melakukannya, tidak ada versi gratisnya, atau tidak ada pembeda yang jelas, itu juga dianggap sebagai nilai.

Pada titik ini, saya mulai bertanya-tanya: apakah ada sesuatu yang seperti bagan Gantt, tetapi sebenarnya bukan bagan Gantt?

Dan kemudian sebuah gambaran terbentuk di benak saya.

Saya ingat ketika saya menggunakan bagan Gantt, saya cenderung meletakkan hal-hal yang lebih penting jauh di bawah.

Item paling bawah biasanya merupakan gambaran besar kondisi untuk menyelesaikan keseluruhan proyek — atau mewakili proyek itu sendiri.

Namun bagaimana jika ada item yang bahkan berada di bawah baris terbawah tersebut — item yang bahkan lebih penting? Apa itu?

Ya, masih banyak hal yang lebih penting - semuanya tidak ada hubungannya dengan pekerjaan. Itu tentang aku. Tentang kehidupan.

Dan ternyata berhasil: Saya tidak akan membuat diagram Gantt bisnis biasa. Saya akan membuat **bagan Gantt kehidupan**.

![](/images/gantt-planet-chart-en.png)

## Langkah Selanjutnya

Jadi saya memutuskan untuk membuat diagram Gantt yang berangkat dari kasus penggunaan bisnis pada umumnya.

Artinya, saya tidak perlu lagi berintegrasi dengan layanan online,

karena sekarang semuanya tentang pengguna — hanya mereka, dan tidak ada yang lain.

Dengan itu, saya telah mengambil satu langkah maju dan mempertahankan proyek ini tetap berjalan untuk saat ini. Tapi bisakah hal itu menghasilkan substansi yang cukup untuk menjadi lengkap?

Saya memikirkan tentang manajemen diri dan hal-hal penting namun tidak mendesak dalam hidup - semuanya memiliki ritme dan frekuensi.

Kesehatan penting, sehingga perusahaan melakukan pemeriksaan tahunan. Keluarga penting, jadi pastikan untuk bertemu dengan orang yang Anda cintai sebelum terlalu banyak waktu berlalu.

Dikombinasikan dengan sifat bagan Gantt, dalam jangka waktu tertentu, item tumpang tindih pada hari ini.

Dan jika Anda mempertimbangkan rentang seumur hidup, setiap item berpotensi relevan saat ini. Itu berarti saya bisa menciutkan semuanya ke garis tengah UI.

Ini memecahkan masalah UI yang sempit sambil mengekspresikan serangkaian nilai yang menurut saya sangat berarti.

![Tampilan utama garis waktu](/images/screenshots/gantt-planet/timeline-en.png)
*Tampilan garis waktu sebenarnya: semua item kehidupan berkumpul di garis tengah kalender — lihat sekilas semua hal penting hari ini*

## Kelengkapan

Salah satu pedoman peninjauan App Store adalah aplikasi Anda tidak bisa hanya meniru apa yang bisa dilakukan halaman web teks biasa.

Misalnya, daftar tugas yang sederhana mungkin tidak bisa diterima. Jadi saya harus memastikan aplikasi ini lebih dari sekadar spreadsheet — jika tidak, Google Spreadsheet dapat melakukan hal yang sama.

Alur visual dari atas ke bawah pada spreadsheet mengingatkan saya untuk menggali ke bawah — seperti setiap hari Anda hanya melakukan tugas minimum di tingkat permukaan. Ada ungkapan Tiongkok, “orang-orang melayang di atas pekerjaannya,” yang menggambarkan keadaan ini dengan sempurna.

Metafora item yang lebih penting yang berada di lapisan yang lebih dalam membuat saya ingin membuatnya lebih visual, lebih nyata. Hubungan langsungnya adalah penggalian - penggalian melalui strata geologi, penambangan.

Lalu muncul pertanyaan tentang implementasi. Haruskah saya sedikit membengkokkan setiap baris spreadsheet? Tambahkan beberapa distorsi perspektif?

Saya memikirkan tentang konteks kehidupan Gantt chart ini - menyendiri dan introspektif.

Gambaran yang terlintas di benak saya adalah: di permukaan kerak planet, ada satu orang yang menggali sendirian. Dan kemudian aku tersadar — bukankah itu anak laki-laki berambut emas yang menyirami mawarnya dan menjinakkan rubah?

Jadi saya membuat bagan Gantt versi 3D, menggunakan poros tambang dan batu permata sebagai representasi visual dari tugas yang harus dilakukan.

Pendekatan yang lebih radikal adalah dengan hanya mempertahankan versi planetnya, namun mengingat kegunaannya, kesulitan peninjauannya, dan seberapa intuitifnya untuk memahaminya, saya memutuskan untuk mempertahankan kedua pandangan tersebut.

![](/images/gantt-planet-3d-en.png)

![Tampilan Planet 3D](/images/screenshots/gantt-planet/geo-view-en.png)
*Bagan Gantt planet 3D — poros tambang dan batu permata sebagai representasi visual dari tujuan hidup*

## Masih Hilang Meja

Dulu ketika saya masih di sekolah, saya menghabiskan banyak waktu untuk duduk dengan nyaman di meja kerja, sendirian — baik untuk belajar atau menulis.

Menggunakan dan memikirkan kehidupan ini Gantt chart terasa seperti membawa saya kembali ke meja itu - meja yang sudah lama dibuang.

Jika saya menyelesaikan sesuatu, saya hanya melakukannya setiap tiga bulan sekali atau setahun sekali — atau bahkan tujuan jangka panjang —

Saya rasa saya sangat ingin menulis di jurnal, atau mungkin menulis surat untuk teman dekat.

Saya menyadari bahwa bagan Gantt ini masih belum memiliki penyaluran emosi terakhir. Namun jika saya menambahkan berbagi media sosial, pengguna tidak akan bisa jujur ​​sepenuhnya.

Opsi lainnya adalah perpesanan dalam aplikasi antar pengguna, namun — saat ini atau di masa depan — jumlah instalasi yang cukup untuk mendukung hal tersebut, atau setidaknya versi Android juga harus tersedia. Bagaimanapun, itu tidak diperlukan untuk versi pertama.

Solusi paling konsisten yang saya dapatkan adalah solusi paling serbaguna: chatbot.

Beri chatbot banyak karya sastra klasik dan biarkan ia memainkan peran sebagai "lubang pohon" — orang kepercayaan — yang menawarkan masukan yang bijaksana kepada pengguna.

## Pikiran Terakhir

Itulah pengembangan produk dan pengambilan keputusan di balik aplikasi ini.

Sepertinya saya terus mengubah arah hingga selesai, namun kenyataannya, ada banyak sekali ide yang terbuang dan fitur yang ditolak yang bahkan belum saya sebutkan.

Selain memberikan gambaran kepada teman-teman yang penasaran tentang jenis-jenis pertimbangan yang digunakan dalam pengembangan produk,

Hal terakhir yang ingin saya tekankan — dan jawaban dari judulnya — adalah bahwa niche dan pertimbangan pengembang indie adalah: **melakukan apa pun yang membuat Anda bahagia!**

Saya yakin banyak orang akan menganggap ini terlalu khusus, atau tidak sesuai dengan selera atau nilai mereka.

Namun demikian, dengan sedikit waktu dan bantuan AI, Anda dapat membangun hal yang Anda inginkan yang belum ada.

Anda harus menjadi bos — memutuskan apa yang berharga dan apa yang layak untuk dibangun.

Anda bisa menjadi desainer — memilih tata letak, warna, font, dan gambar favorit Anda.

Anda harus menjadi PM — memutuskan bagaimana menulisnya dan seberapa lengkap fitur-fiturnya.

AI hanya akan menjadi lebih kuat. Meski saat ini tidak bisa melakukan semuanya, di masa mendatang, Anda juga akan bisa menikmati semua ini.

App Store kini menjadi beranda pribadi era baru — setiap orang dapat mempublikasikan kisah mereka sendiri.

Jika Anda tertarik, ikuti blog ini. Saya akan terus berbagi pengalaman dan refleksi nyata dari publikasi di App Store.
