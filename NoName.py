import random
import time
import os

def main():
    os.system ('clear')
    os.system ('figlet -f banner3-D.flf NoName | lolcat')
    banner = ''
    print (banner)
main()

text = "Selamat , datang di NoName !! -->"
for char in text:
    print(char, end='', flush=True)
    time.sleep(0,1)
print()

print("-->Hacking is caring")
text = [
    "--> Kami berjalan bersama rakyat <--",
    "Peraturan seharusnya memberikan solusi , bukan merugikan rakyat kecil",
    "Jadi jangan seenaknya !!!"
]

for line in text:
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0,1)

def random_name_generator():
    first_name =["apakah nama kamu haryanto", "apakah nama kamu mansur"]
    last_name =["jasoon ..?" , "sandy..?" , "jones..?" , "fredy ..?"]
    full_name = random.choice(first_name) +" "+ random.choice(last_name)
    return full_name

def main():
    while True:
        print("gas ajad dulu curhat belkangan...")
        time.sleep(2)
        print("Bersiaplah untuk keadilan yg sebenarnya"), random_name_generator()

        again = input("mau ganti nama g bree (ya/no)?")
        if again.lower() != "ya":
            break

if __name__ == "__main__":
 main()