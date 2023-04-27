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
    time.sleep(0.1)
print()

print (" ____ ____ ____ ____ ")
print ("||N |||o |||N |||a ||")
print ("||__|||__|||__|||me||")
print ("|/__\|/__\|/__\|/__\|")


print("--> Hacking is caring <--")
text = [
    "--> Kami berjalan bersama rakyat <--",
    "Peraturan seharusnya memberikan solusi , bukan merugikan rakyat kecil",
   "Jadi jangan seenaknya !!!"
]

for line in text:
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()


def random_name_generator():
  first_names = ["apakah nama kamu Haryanto", "apakah nama kamu mansur", "apakah nama kamu Oji", "apakah nama kamu mario", "apakah nama kamu indah", "apakah nama kamu Tony", "apakah nama kamu Mia", "apakah nama kamu Susi", "apakah nama kamu dandy", "apkah nama kamu Evelyn"]
  last_names = ["jason ...?", "hawk ...?", "sendy ...?", "Jones ...?", "ray ...?", "fredy ...?", "Miller ...?", "Wilson ...?", "Moore ...?", "Taylor ...?"]
  full_name = random.choice(first_names) + " " + random.choice(last_names)
  return full_name

def main():
  while True:
    print("Gas aja dulu curhat belakangan...")
    time.sleep(2)
    print("Bersiaplah untuk keadilan sebenarnya :", random_name_generator())

    again = input("Mau ganti nama ga bree (ya/no)? ")
    if again.lower() != "ya":
      break

if __name__ == "__main__":
  main()
