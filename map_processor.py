import cv2
import sys
import numpy as np

def process_image(input_path, output_path):
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Image not found or unable to read")
        sys.exit()

    smoothed = smooth_edges(image)
    smoothed_color = cv2.cvtColor(smoothed, cv2.COLOR_GRAY2BGR)
    colored = apply_custom_colormap(smoothed_color)
    
    cv2.imwrite(output_path, colored)
    print(f"Processed image saved as {output_path}")

def smooth_edges(image):
    # 画像を二値化
    _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # 輪郭を検出
    contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭を滑らかに描画
    smoothed = np.zeros_like(image)
    cv2.drawContours(smoothed, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    return smoothed

def apply_custom_colormap(image):
    # LUTを定義
    colors = np.array([
        [255, 182, 193],  # 薄桃色
        [152, 251, 152],    # オレンジ色
        [255, 140, 0],  # 薄い緑色
        # その他のカラー
    ], dtype=np.uint8)

    # 画像の最大値に応じてLUTを適用
    max_value = np.max(image) if np.max(image) > 0 else 1
    lut = np.zeros((256, 1, 3), dtype=np.uint8)
    for i in range(256):
        if i > 200:  # 障害物がないエリア
            lut[i, 0, :] = colors[0]
        elif i > 100:  # 未探索エリア
            lut[i, 0, :] = colors[1]
        else:  # 障害物
            lut[i, 0, :] = colors[2]

    # 画像のデータタイプを確認し、必要に応じて変換
    if image.dtype != np.uint8:
        image = np.uint8(image)

    # LUTを使用してカラーマッピング
    colored_image = cv2.LUT(image, lut.reshape(256, 1, 3))

    return colored_image

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    process_image(input_path, output_path)
