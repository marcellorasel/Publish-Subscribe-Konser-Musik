import paho.mqtt.client as mqtt
import datetime # Untuk mendapatkan waktu dan tanggal

# Nama broker yang akan digunakan
broker_address = 'broker.emqx.io'
# buat client baru 
print("Create new instance")
client = mqtt.Client("Publisher")
# lakukan koneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port = 1883)

#Fungsi menampilkan pilihan agensi
def agensi():
    global topic
    SMT = "SMTown"
    YGE = "YG Entertainment"
    print("===================================================================================================")
    print("Daftar Agensi : \n 1. SMTown \n 2. YG Entertainment \n Masukkan pilihan (ketik '1' atau '2') :")
    i = input()
    if i == str(1):
        topic = SMT
    elif i == str(2):
        topic = YGE
    print("===================================================================================================")

# Publish Jadwal ke Subscriber
def publish(client):
    i = 1
    while (i == 1):
        print("Mempublish Jadwal Konser")
        jadwal = datetime.datetime.strptime(
            input('Informasikan jadwal konser dengan format TAHUN/BULAN/HARI - JAM:MENIT : '), "%Y/%m/%d - %H:%M"
        )
        pesan = f"Informasi Jadwal Konser {topic} berlangsung pada : {jadwal}"
        #Publish pesan ke Broker
        jadwal_konser = client.publish(topic, pesan)
        print(f"Mengirim {pesan} ke Subscriber {topic}")
        print("Jadwal konser telah terkirim")
        print("===================================================================================================")
        print("Ketik 'Publish lagi' untuk publish lagi atau ketik 'Close' untuk keluar : ")
        j = input()
        if j == ("Publish lagi"):
            print("===================================================================================================")
        elif j == ("Close"):
            break

def main():
    agensi()
    print(topic)
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    main()