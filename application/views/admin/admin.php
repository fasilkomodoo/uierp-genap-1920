<div class="card">
    <div class="card-header bg-white my-3">
        <h2 class="card-title">
            Welcome
        </h2>
    </div>
    <div class="card-body">
        <p>
            Aplikasi PUR_CHASE (pur·chase /ˈpərCHəs/) merupakan aplikasi yang bersifat sebagai proxy dari modul purchase Odoo.
            Pengembangan aplikasi ini dimulai untuk memenuhi kebutuhan tugas akhir mata kuliah konfigurasi ERP dari pengembang, Nathanael.
        </p>

        <p class="lead">
            Sedikit histori dan fakta pengembangan PUR_CHASE
        </p>
        <ul>
            <li>
                Dimulai pada 19 Mei 2020
            </li>
            <li>
                Direncanakan untuk selesai pada tanggal 14 Juni 2020 (batas UAS Konfigurasi ERP)
            </li>
            <li>
                Awalnya dirancang sebagai aplikasi android yang dikembangkan menggunakan Flutter, namun tanggal 10 Juli 2020, dependensi modul JSON API Odoo yang menjadi dependensi utama PUR_CHASE Flutter ditarik dari http://apps.odoo.com/ dan saya tidak memiliki cukup waktu untuk mempelajari implementasi XML-RPC Odoo sebagai pengganti JSON API di Flutter.
            </li>
            <li>
                11 Juli 2020, Saya mengubah seluruh backend PUR_CHASE dari Framework Flutter dengan bahasa Dart menjadi Framework CodeIgniter 3 dengan bahasa PHP dengan harapan bahwa aplikasi dapat diubah menjadi <a href="https://developers.google.com/web/ilt/pwa">PWA (progressive web application)</a> selesai dengan modul utama pada tanggal 14 Juli 2020.
            </li>
            <li>
                12 Juli 2020, Saya mempelajari XML-RPC dari situs resmi, forum, dan referensi Odoo lainnya. Saya belum sempat mengimplementasikannya karena saya sedang magang full-time juga.
            </li>
            <li>
                13 Juli 2020, Saya menggunakan MDBootstrap sebagai template aplikasi dan mencoba berkomunikasi dengan Odoo melalui XML-RPC CodeIgniter dengan bantuan library "riptide". Saya juga berhasil mengubah response XML-RPC dari Odoo menjadi JSON menggunakan PHP. Saya berhasil mengimplementasikan READ daftar Supplier.
            </li>
            <li>
                14 Juli 2020, Saya kekurangan waktu untuk mengubah aplikasi dalam 4 hari terakhir dan masih mengembangkan PUR_CHASE dengan target create RFQ pada hari minggu, 19 Juli 2020.
            </li>
        </ul>
    </div>
</div>