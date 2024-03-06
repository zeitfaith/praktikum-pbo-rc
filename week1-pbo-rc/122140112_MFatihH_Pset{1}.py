import random

class Robot:
    def __init__(self, nama, max_hp, kekuatan_serang, akurasi_serang):
        self.nama = nama
        self.max_hp = max_hp
        self.hp = max_hp
        self.kekuatan_serang = kekuatan_serang
        self.akurasi_serang = akurasi_serang

    def serang_musuh(self, musuh):
        if random.random() < self.akurasi_serang:
            damage = random.randint(1, self.kekuatan_serang)
            musuh.menerima_serangan(damage)
            print(f"{self.nama} menyerang {musuh.nama} dan menyebabkan kerusakan {damage} poin.")
        else:
            print(f"Serangan {self.nama} meleset!")

    def menerima_serangan(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.nama} menerima kerusakan sebesar {damage} poin. HP {self.nama}: {self.hp}")

    def perbarui_kesehatan(self):
        jumlah_regen = random.randint(1, 10)
        self.hp += jumlah_regen
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.nama} meregenerasi {jumlah_regen} HP. HP {self.nama}: {self.hp}")


class Permainan:
    def __init__(self, putaran):
        self.putaran = putaran

    def mulai_permainan(self, robot1, robot2):
        print("Permainan Dimulai!")
        for nomor_putaran in range(1, self.putaran + 1):
            print(f"Putaran {nomor_putaran}:")
            robot1.serang_musuh(robot2)
            if robot2.hp <= 0:
                print(f"{robot1.nama} menang!")
                break
            robot2.serang_musuh(robot1)
            if robot1.hp <= 0:
                print(f"{robot2.nama} menang!")
                break


# Contoh penggunaan
robot1 = Robot("Robot1", 100, 20, 0.8)
robot2 = Robot("Robot2", 120, 15, 0.9)
permainan = Permainan(10)
permainan.mulai_permainan(robot1, robot2)
