import os
import qrcode
import pandas as pd
import sys

def generate_qr_code(url, save_path="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
    print(f"QR code saved as {save_path}")

if __name__ == "__main__":
    assert "--csv_file_path" in sys.argv
    csv_file_path = sys.argv[sys.argv.index("--csv_file_path") + 1]
    df = pd.read_csv(csv_file_path)
    reg_links_column = "Registration Link(s) - General link : https://www.gitalifenyc.com/events?register=true"
    qr_codes_links_column = "QR Codes Links"
    github_repo_url = "https://github.com/Akhil-Raj/automatic_whatsapp_messenger/blob/main"
    for index, url in enumerate(df[reg_links_column]):
        if "=" in str(url):
            file_name = url.split("=")[-1] + ".png"
            save_path = f"qr_codes/{file_name}"
            generate_qr_code(url, save_path = save_path)
            df.loc[index, qr_codes_links_column] = os.path.join(github_repo_url, save_path)
    df.to_csv(csv_file_path)