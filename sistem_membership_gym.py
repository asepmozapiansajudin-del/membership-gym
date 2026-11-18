from datetime import datetime, timedelta
from abc import ABC, abstractmethod


# =====================================
# CLASS MEMBERSHIP (ABSTRACTION)
# =====================================

class Membership(ABC):

    def __init__(self, nama_paket, harga):
        self.nama_paket = nama_paket
        self.harga = harga

    @abstractmethod
    def hitung_harga(self):
        pass

    def __str__(self):
        return f"{self.nama_paket} - Rp{self.hitung_harga():,}"


# =====================================
# INHERITANCE: REGULAR MEMBERSHIP
# =====================================

class RegularMembership(Membership):

    def hitung_harga(self):
        return self.harga


# =====================================
# INHERITANCE: PREMIUM MEMBERSHIP
# =====================================

class PremiumMembership(Membership):

    def hitung_harga(self):
        return self.harga + 100000


# =====================================
# CLASS MEMBER
# =====================================

class Member:

    jumlah_member = 0

    def __init__(self, id_member, nama, umur, paket):
        self.id_member = id_member
        self.__nama = nama
        self.__umur = umur
        self.paket = paket
        self.tanggal_daftar = datetime.now()
        self.tanggal_akhir = (
            self.tanggal_daftar + timedelta(days=30)
        )
        self.riwayat_checkin = []

        Member.jumlah_member += 1

    # ENCAPSULATION: GETTER
    @property
    def nama(self):
        return self.__nama

    # ENCAPSULATION: SETTER
    @nama.setter
    def nama(self, nama_baru):
        if nama_baru.strip():
            self.__nama = nama_baru
        else:
            print("Nama tidak boleh kosong!")

    @property
    def umur(self):
        return self.__umur

    # MENGHITUNG BIAYA
    def biaya_membership(self):
        return self.paket.hitung_harga()

    # MEMPERPANJANG MEMBERSHIP
    def perpanjang(self):
        self.tanggal_akhir += timedelta(days=30)

    # CHECK IN
    def checkin(self):
        if datetime.now() > self.tanggal_akhir:
            print("Membership sudah tidak aktif!")
            return

        waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.riwayat_checkin.append(waktu)

        print("Check-in berhasil!")

    # CLASS METHOD
    @classmethod
    def total_member(cls):
        return cls.jumlah_member

    # STATIC METHOD
    @staticmethod
    def validasi_umur(umur):
        return umur >= 15

    # SPECIAL METHOD
    def __str__(self):
        return (
            f"ID Member : {self.id_member}\n"
            f"Nama      : {self.nama}\n"
            f"Umur      : {self.umur} tahun\n"
            f"Paket     : {self.paket.nama_paket}\n"
            f"Biaya     : Rp{self.biaya_membership():,}\n"
            f"Berakhir  : {self.tanggal_akhir.strftime('%d-%m-%Y')}"
        )


# =====================================
# CLASS UTAMA GYM
# =====================================

class Gym:

    def __init__(self):
        self.daftar_member = []
        self.nomor_member = 1

    # MENAMPILKAN PAKET
    def tampilkan_paket(self):
        print("\n===== PILIH PAKET MEMBERSHIP =====")
        print("1. Regular  - Rp200.000")
        print("2. Premium  - Rp300.000")

    # PENDAFTARAN MEMBER
    def tambah_member(self):
        print("\n===== PENDAFTARAN MEMBER =====")

        nama = input("Masukkan nama: ")

        try:
            umur = int(input("Masukkan umur: "))

            if not Member.validasi_umur(umur):
                print("Umur minimal 15 tahun!")
                return

        except ValueError:
            print("Umur harus berupa angka!")
            return

        self.tampilkan_paket()

        pilihan = input("Pilih paket (1/2): ")

        if pilihan == "1":
            paket = RegularMembership("Regular", 200000)

        elif pilihan == "2":
            paket = PremiumMembership("Premium", 200000)

        else:
            print("Pilihan paket tidak tersedia!")
            return

        member = Member(
            f"G{self.nomor_member:03d}",
            nama,
            umur,
            paket
        )

        self.daftar_member.append(member)
        self.nomor_member += 1

        print("\nPendaftaran berhasil!")
        print(member)

    # MENAMPILKAN DATA MEMBER
    def tampilkan_member(self):
        print("\n===== DATA MEMBER GYM =====")

        if not self.daftar_member:
            print("Belum ada anggota terdaftar.")
            return

        for member in self.daftar_member:
            print("--------------------------")
            print(member)

    # MENCARI MEMBER
    def cari_member(self, id_member):
        for member in self.daftar_member:
            if member.id_member == id_member:
                return member
        return None

    # MEMPERPANJANG MEMBERSHIP
    def perpanjang_member(self):
        print("\n===== PERPANJANG MEMBERSHIP =====")

        id_member = input("Masukkan ID Member: ")
        member = self.cari_member(id_member)

        if member:
            member.perpanjang()
            print("Membership berhasil diperpanjang!")
            print("Tanggal akhir:", 
                  member.tanggal_akhir.strftime("%d-%m-%Y"))
        else:
            print("Member tidak ditemukan!")

    # CHECK IN MEMBER
    def checkin_member(self):
        print("\n===== CHECK IN GYM =====")

        id_member = input("Masukkan ID Member: ")
        member = self.cari_member(id_member)

        if member:
            member.checkin()
        else:
            print("Member tidak ditemukan!")

    # RIWAYAT CHECK IN
    def riwayat_member(self):
        print("\n===== RIWAYAT CHECK IN =====")

        id_member = input("Masukkan ID Member: ")
        member = self.cari_member(id_member)

        if member:
            if member.riwayat_checkin:
                for data in member.riwayat_checkin:
                    print(data)
            else:
                print("Belum ada riwayat check-in.")
        else:
            print("Member tidak ditemukan!")


# =====================================
# PROGRAM UTAMA
# =====================================

def main():

    gym = Gym()

    while True:

        print("\n================================")
        print("    APLIKASI MEMBERSHIP GYM")
        print("================================")
        print("1. Daftar Member")
        print("2. Tampilkan Data Member")
        print("3. Perpanjang Membership")
        print("4. Check-in Gym")
        print("5. Riwayat Check-in")
        print("6. Total Member")
        print("7. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            gym.tambah_member()

        elif pilihan == "2":
            gym.tampilkan_member()

        elif pilihan == "3":
            gym.perpanjang_member()

        elif pilihan == "4":
            gym.checkin_member()

        elif pilihan == "5":
            gym.riwayat_member()

        elif pilihan == "6":
            print(
                "Total Member:",
                Member.total_member()
            )

        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid!")


# MENJALANKAN PROGRAM

if __name__ == "__main__":
    main()
