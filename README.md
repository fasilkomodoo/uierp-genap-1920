# UAS Konfigurasi ERP — Extra Modul (Pengembangan Modul Point of Sale User List and Status)
Modul ini dibuat untuk memenuhi soal UAS Konfigurasi ERP nomor 8. Dokumentasi lengkap dari pengembangan modul dan cara menggunakannya dapat diakses pada [link ini](https://docs.google.com/document/d/1BZWd8ZtUjk1xdyv_W0l4edCf1kWuAjX3AclQisnUt48/edit?usp=sharing) atau [link ini](https://medium.com/@scoobydoo.uierp1/uas-konfigurasi-erp-extra-modul-b52981e9861a). Video instalasi dan tutorial penggunaan dapat diakses pada [link ini](https://www.youtube.com/watch?v=RyqTM4vETgI).

# Ide Pengembangan Awal
## Latar Belakang
Pada Odoo 10, tampilan dari laporan untuk transaksi yang dilakukan melalui Point of Sale memiliki tampilan yang cukup sulit untuk dikendalikan dan dipahami. Hal ini dapat membuat pengguna mengalami kesulitan dalam mencari informasi penting seperti jumlah produk yang terjual dan jumlah pelanggan yang membeli produk. Untuk mengatasi hal ini, dapat dibuat suatu modul untuk menghasilkan laporan yang lebih mudah untuk digunakan dan dipahami.

## Ruang Lingkup
Modul yang akan dikembangkan akan membutuhkan modul Point of Sales dan menggunakan data transaksi yang dilakukan pada modul tersebut.

## Rencana Fitur
Modul akan dapat diakses pada menu ‘Report’ yang akan dikembangkan atau menjadi sub menu dari ‘Point of Sales’ > ‘Report’. Setelah menu tersebut dapat diakses, pengguna dapat memilih beberapa jenis laporan yang mengandung beberapa informasi berbeda seperti jumlah penjualan produk dan jumlah pembelian yang dilakukan oleh pelanggan.

# Ide Pengembangan Terbaru
## Latar Belakang
Saat menggunakan modul Point of Sale, satu konfigurasi point of sale mungkin digunakan oleh lebih dari satu orang pada suatu periode tertentu. Hal ini mungkin terjadi karena terdapat kerusakan pada hardware point of sale atau gangguan lainnya atau pekerja yang berhalangan hadir dan harus digantikan. Kejadian-kejadian seperti itu tentunya harus terekam dengan baik untuk menghindari adanya fraud. Selain itu, status dari konfigurasi point of sale juga harus selalu diperbarui agar perusahaan dapat mengetahui apakah terdapat tindakan yang perlu dilakukan agar modul Point of Sale dapat berjalan dengan baik.

## Ruang Lingkup
Modul yang akan dikembangkan akan membutuhkan modul Point of Sales dan menggunakan data konfigurasi point of sale dan pengguna Odoo.

## Rencana Fitur
Modul akan dapat diakses melalui sub menu ‘Point of Sale’ > ‘Reports > User List and Status’. Setelah menu tersebut dapat diakses, pengguna dapat melihat, mengubah, dan menambahkan informasi terkait pengguna dan status dari konfigurasi point of sale setiap harinya. 
