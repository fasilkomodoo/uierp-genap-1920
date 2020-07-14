#Ide Pengembangan Awal

##Latar Belakang
Pada Odoo 10 modul Purchases dan Invoicing setelah melakukan konfirmasi dan verifikasi dari purchase order dilanjutkan proses billing. Namun hal ini tidak terdapat proses shipment plan. Modul shipping saat ini masih belum ada di Odoo dan tidak terintegrasi dengan modul apapun. Sebelumnya kita mengetahui bahwa proses selanjutnya dari sales order adalah shipping atau pengiriman barang kepada pelanggan. Seperti halnya sales order entry, proses bisnis shipping atau pengiriman barang ini juga termasuk dalam revenue cycle atau siklus pendapatan dalam perusahaan. Kita juga telah mempelajari bahwa setiap perusahaan harus memiliki revenue cycle atau memiliki siklus pendapatan agar perusahaan tetap hidup dan bertumbuh. Oleh karena itu proses ini merupakan proses yang sangat penting dalam menunjang proses bisnis perusahaan dalam Order Fulfilment.

##Ruang Lingkup
Modul yang akan dikembangkan akan membutuhkan modul Purchases dan menggunakan data transaksi yang dilakukan pada modul tersebut.
Rencana Fitur
Modul akan dapat diakses melalui sub menu ‘Purchases’ > ‘Purchase > Shipment’. Setelah menu tersebut dapat diakses, pengguna dapat melihat, mengubah, dan menambahkan informasi terkait shipping plan yang terintegrasi dengan Purchase Order.
Pengembangan Selanjutnya
Pada pengembangan selanjutnya modul ini dapat dibuat dengan adanya integrasi dengan ekspedisi yang tersedia yang sudah dibuat (terdapat menu ekspedisi) selain itu juga dapat dibuat kustomisasi untuk melakukan ekspedisi menggunakan jasa atau perusahaan sendiri. Pengembangan kedepannya adalah mengintegrasi dengan modul Packing dan Warehouse Management.

#Cara melakukan instalasi modul add on custom pada Odoo 10
Pastikan modul yang dibuat sudah terletak pada folder \Odoo 10.0\server\odoo\addons

1. Pull melalui github.com/ dan kemudian masukan ke folder add-ons
2. Masuk ke odoo dan ke menu settings lalu pilih “Activate Developer Mode”
3. Pada menu “Apps” pilih Update Apps List
4. Kemudian lakukan pencarian modul dan lakukan instalasi
5. Modul berhasil di install dan bisa dilihat pada bagian Purchases

#Modul Shipment Plan

##Kegunaan modul
1. Membuat perencanaan pengiriman barang ke pelanggan melalui perusahaan ekspedisi atau menggunakan pengiriman perusahaan.
2. Di sini tim logistik dapat mengetahui rencana shipping yang akan dilakukan setelah purchase order berhasil dikonfirmasi.
3. Untuk perusahaan yang menggunakan aplikasi terintegrasi maka informasi pengiriman barang ini akan diketahui oleh bagian penagihan untuk selanjutnya ditindaklanjuti pembuatan tagihan kepada pelanggan. 
4. Terdapat informasi yang lengkap mengenai detail pengiriman yang harus dilakukan, ini untuk menambah efektifitas dari bagian warehouse dan sales.

##Perbedaan sebelum dan sesudah modul add on diinstall

Perbedaannya adalah terdapat fitur baru dari shipment plan pada menu Purchase -> Shipment dan fitur yang bisa diakses

