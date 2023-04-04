import sys
import os
from PIL import Image

def main(file_path):
    # 画像ファイルの拡張子をチェックする
    if not file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        print("画像ファイルはjpgまたはpng形式である必要があります。")
        sys.exit(1)

    # 画像ファイルを読み込む
    image = Image.open(file_path)

    # 画像をRGBモードに変換する
    image = image.convert('RGB')

    # 各ピクセルのRGB値の合計とピクセル数を初期化
    total_rgb = [0, 0, 0]
    pixel_count = 0

    # 画像の各ピクセルをループし、RGB値を合計する
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            total_rgb[0] += r
            total_rgb[1] += g
            total_rgb[2] += b
            pixel_count += 1

    # RGB値の平均を計算する
    average_rgb = [round(value / pixel_count) for value in total_rgb]

    # 平均RGB値を出力する
    print("平均RGB値:", average_rgb)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法：python <このスクリプトの名前> <画像ファイルへのパス>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
