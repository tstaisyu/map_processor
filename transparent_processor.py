import sys
from PIL import Image

def convert_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")  # RGBAモードに変換してアルファチャンネルを追加

        datas = img.getdata()

        newData = []
        for item in datas:
            # 未探索エリアのグレースケール値205をチェック
            if item[0] == 205 and item[1] == 205 and item[2] == 205:
                newData.append((255, 255, 255, 0))  # 透明に変更
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")  # PNGフォーマットで保存
        print(f"Converted image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    convert_image(input_path, output_path)
