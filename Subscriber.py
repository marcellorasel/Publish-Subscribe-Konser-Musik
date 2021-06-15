import paho.mqtt.client as mqtt
import time # Untuk sleep()

# Nama broker yang akan digunakan
broker_address = 'broker.emqx.io'

# Fungsi menerima pesan dari Publisher
def on_message(client, userdata, msg):
    print("===================================================================================================")
    print("Pesan diterima : ",str(msg.payload.decode("utf-8")), f" dari {msg.topic}")

# Fungsi menu pilihan subscribe agensi
subscribe_agensi = []
def menu(client):
    SMT = "SMTown"
    YGE = "YG Entertainment"
    print("===================================================================================================")
    print(f"Pilih Agensi untuk di-Subscribe : \n 1. {SMT} \n 2. {YGE} \n Masukkan pilihan (ketik '1' atau '2') : ")
    i = input()
    if i == str(1):
        print("===================================================================================================")
        print("Subscribe-Unsubscribe Agensi : \n Subscribe \n Unsubscribe \n Masukkan pilihan (ketik 'Subscribe' atau 'Unsubscribe') :")
        j = input()
        if j == "Subscribe":
            if SMT in subscribe_agensi:
                print("Anda sudah men-subscribe SMTown")
            else:
                subscribe_agensi.append(SMT)
                client.subscribe(SMT)
                print("Berhasil men-subscribe SMTown")
        elif j == "Unsubscribe":
            if SMT in subscribe_agensi:
                subscribe_agensi.pop(subscribe_agensi.index(SMT))
                client.unsubscribe(SMT)
                print("Berhasil men-unsubscribe SMTown")
            else:
                print("Anda belum men-subscribe SMTown")
    elif i == str(2):
        print("Subscribe-Unsubscribe Agensi : \n Subscribe \n Unsubscribe \n Masukkan pilihan (ketik 'Subscribe' atau 'Unsubscribe') :")
        j = input()
        if j == "Subscribe":
            if YGE in subscribe_agensi:
                print("Anda sudah men-subscribe YG Entertainment")
            else:
                subscribe_agensi.append(YGE)
                client.subscribe(YGE)
                print("Berhasil men-subscribe YG Entertainment")
        elif j == "Unsubscribe":
            if YGE in subscribe_agensi:
                subscribe_agensi.pop(subscribe_agensi.index(YGE))
                client.unsubscribe(YGE)
                print("Berhasil men-unsubscribe YG Entertainment")
            else:
                print("Anda belum men-subscribe YG Entertainment")
    print(f"Daftar Agensi yang Anda subscribe : {subscribe_agensi}") 
    print("===================================================================================================") 
    print("Ketik 'Menu' untuk menampilkan menu atau ketik 'Close' untuk keluar :")          

def main():
    # Buat client baru
    print("Create new instance")
    client = mqtt.Client("Subscriber")

    # Lakukan koneksi ke broker
    print("Connecting to broker")
    client.connect(broker_address, port = 1883)

    # Start Loop Client
    client.loop_start()
    time.sleep(1)

    menu(client)
    while True:
        client.on_message = on_message
        i = input()
        if (i == "Menu"):
            menu(client)
        elif (i == "Close"):
            break
        time.sleep(1)

if __name__ == '__main__':
    main() 