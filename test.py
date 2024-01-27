import pandas as pd
import pantab
import io
from chardet.universaldetector import UniversalDetector

def main():
    file_path = 'c01.csv'
    detector = UniversalDetector()
    with open(file_path, mode='rb') as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    print(detector.result, end='')
    print(detector.result['encoding'], end='')

    csv_encoding = detector.result['encoding']
    # CSVを文字コードを指定して読み込み、Hyperファイルに変換
    df = pd.read_csv('c01.csv', encoding='CP932')
    # hyper作成
    pantab.frame_to_hyper(df, 'sample.hyper', table='table')


if __name__ == "__main__":
    main()







