import instaloader

# Buat instance Instaloader
loader = instaloader.Instaloader()

# Fungsi untuk mengunduh postingan Instagram berdasarkan URL
def download_post(url):
    try:
        # Mendapatkan metadata postingan
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

        # Mengunduh postingan
        loader.download_post(post, target="testcoki")
        print("Postingan berhasil diunduh!")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

# Demo Program
url = input("Enter your url: ")
url = str(url)
download_post(url)
