# UAS Konfigurasi ERP — Extra Modul — Pengembangan Modul Human Resourse (Employee) Dengan Penambahan ID Employee
Modul ini dibuat untuk memenuhi soal UAS Konfigurasi ERP nomor 8. Dokumentasi lengkap dari pengembangan modul dan cara menggunakannya dapat diakses pada [Medium](https://medium.com/@hachi.uierp1/uas-soal-8-extra-modul-110c3ab61aa0) atau [Google Docs](https://docs.google.com/document/d/1zNCpZPE3IukBDXFuRpeeMxMWxu36gQfXYMe0lTV6snU/edit?usp=sharing). Video instalasi dan simulasi penggunaan dapat diakses pada [Youtube](https://youtu.be/JUwYgzocfiU).

# Ide Pengembangan Awal
## Latar Belakang
Pada Odoo 12, karyawan (employee) hanya dapat ditambahkan satu persatu. Pada perusahaan yang baru mengimplementasi Odoo, memasukkan data karyawan akan memakan waktu yang tidak sedikit. Pengadaan fitur import employee dirasa kurang tepat digunakan mengingat banyaknya constraint dalam menambahkan karyawan baru. Oleh karena itu, diperlukan fitur (bukan fitur import) yang dapat memasukkan data banyak karyawan melalui interface Odoo dengan effort yang lebih sedikit.

## Ruang Lingkup
Modul yang akan dikembangkan akan membutuhkan modul Point of Sales dan menggunakan data transaksi yang dilakukan pada modul tersebut.

## Rencana Fitur
Fitur akan ditaruh pada menu ‘Employees’. Untuk menambahkan karyawan, pengguna harus menekan ‘Create’ terlebih dahulu. Lalu, pengguna dapat memilih untuk menambahkan karyawan lainnya tanpa perlu menyimpan data karyawan sebelumnya dengan menekan tombol ‘Add New Employee’. Setelah memasukkan data beberapa karyawan, pengguna menekan tombol ‘Save’ dan semua data karyawan akan tersimpan.

# Ide Pengembangan Terbaru
## Latar Belakang
Pada Odoo 12, karyawan (employee) hanya memiliki ID yang diperoleh dari database saat melakukan input data karyawan. Beberapa perusahaan membedakan ID yang berada di database dan ID yang diperoleh karyawan ketika ia diterima untuk bekerja di perusahaan. Dengan adanya tambahan field ID yang dimiliki oleh karyawan, diharapkan pencarian karyawan dapat menjadi lebih mudah.

## Ruang Lingkup
Modul yang akan dikembangkan termasuk ke dalam kategori Human Resource. Modul ini membutuhkan apps Employee (hr) untuk dapat digunakan.

## Rencana Fitur
Fitur akan ditaruh pada menu ‘Employees’. Ketika menambahkan karyawan atau mengubah informasi karyawan, terdapat field baru yang bernama Employee’s ID. Setelah perubahan disimpan, ID milik karyawan tersebut dapat dilihat.
