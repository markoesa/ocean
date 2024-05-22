import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Fungsi untuk membaca konten dari file privat.txt sebagai daftar baris
def read_texts_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return []

# Fungsi untuk menjalankan tugas utama
def run_task(textarea_text):
    # Konfigurasi driver
    options = uc.ChromeOptions()
    options.headless = True  # Set to True to run the browser in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Inisialisasi driver
    driver = uc.Chrome(options=options)

    # Buka URL
    url = 'https://walletapp.waveonsui.com/#tgWebAppData=query_id%3DAAGYddUnAwAAAJh11Sez5s8u%26user%3D%257B%2522id%2522%253A7110751640%252C%2522first_name%2522%253A%2522Resa%2522%252C%2522last_name%2522%253A%2522%2524BTON%2522%252C%2522username%2522%253A%2522resamersa%2522%252C%2522language_code%2522%253A%2522en%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26auth_date%3D1716315855%26hash%3D52512cdf8d3dba657bed6eacdd1f3fb2d6645437b3cb9c1939c7f560fbca0184&tgWebAppVersion=7.2&tgWebAppPlatform=web&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23212121%22%2C%22button_color%22%3A%22%238774e1%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23aaaaaa%22%2C%22link_color%22%3A%22%238774e1%22%2C%22secondary_bg_color%22%3A%22%23181818%22%2C%22text_color%22%3A%22%23ffffff%22%2C%22header_bg_color%22%3A%22%23212121%22%2C%22accent_text_color%22%3A%22%238774e1%22%2C%22section_bg_color%22%3A%22%23212121%22%2C%22section_header_text_color%22%3A%22%238774e1%22%2C%22subtitle_text_color%22%3A%22%23aaaaaa%22%2C%22destructive_text_color%22%3A%22%23ff595a%22%7D'
    driver.get(url)

    # Tunggu halaman untuk memuat sepenuhnya
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-login'))
    )

    # Klik tombol login
    try:
        login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-login')
        login_button.click()
        print("login...")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengklik tombol login: {e}")

    # Tunggu halaman setelah login untuk memuat sepenuhnya
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.h-full.w-full'))
    )

    # Masukkan teks ke dalam textarea
    try:
        textarea = driver.find_element(By.CSS_SELECTOR, 'textarea.h-full.w-full')
        textarea.send_keys(textarea_text)
        print("privatkey telah dimasukkan ke dalam script")
    except Exception as e:
        print(f"Terjadi kesalahan saat memasukkan teks ke dalam script: {e}")

    # Klik tombol Continue
    try:
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-continue.btn-common.w-full'))
        )
        continue_button.click()
        print("Continue...")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengklik tombol Continue: {e}")

    # Klik tombol Claim Now (span)
    try:
        claim_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn_claim'))
        )
        claim_button.click()
        print("Claim")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengklik tombol Claim Now: {e}")

    # Klik elemen berdasarkan XPath
    try:
        xpath_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/section/div/div/div[3]/div[2]/div[2]/div[2]/button/span'))
        )
        xpath_element.click()
        print(".......")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengklik elemen dengan XPath: {e}")

    # Klik tombol Claim Now (div)
    try:
        div_claim_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.claim.cursor-pointer'))
        )
        div_claim_button.click()
        print("Claim Now")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengklik tombol Claim Now (div): {e}")

    # Tunggu beberapa saat untuk melihat hasil
    time.sleep(1)
    # Tutup browser
    driver.quit()

# Baca teks dari file privat.txt sebagai daftar baris
texts = read_texts_from_file('privat.txt')
if not texts:
    print("Gagal membaca teks dari file. Menghentikan script.")
    exit()

# Loop utama
text_index = 0
while True:
    # Dapatkan teks saat ini
    textarea_text = texts[text_index]
    
    # Tampilkan informasi akun yang sedang dikerjakan
    print(f"Mengerjakan akun: {textarea_text}")
    
    # Jalankan tugas utama
    run_task(textarea_text)
    
    # Perbarui index untuk teks berikutnya
    text_index = (text_index + 1) % len(texts)
    
    # Tunggu beberapa saat sebelum mengulangi proses
    time.sleep(1)  # Sesuaikan waktu tunggu sesuai kebutuhan Anda
