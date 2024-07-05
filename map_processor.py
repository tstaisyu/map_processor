import cv2
import sys

def process_image(input_path, output_path):
    # 画像をグレースケールで読み込む
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Image not found or unable to read")
        sys.exit()

    # ガウシアンブラーを適用
    smoothed = cv2.GaussianBlur(image, (5, 5), 0)

    # カラーマッピング
    colored = cv2.applyColorMap(smoothed, cv2.COLORMAP_JET)

    # 画像の保存
    cv2.imwrite(output_path, colored)
    print(f"Processed image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    process_image(input_path, output_path)

