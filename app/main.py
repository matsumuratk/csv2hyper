from flask import Flask, render_template, request, Response
import pandas as pd
import pantab
import io
import os
from chardet.universaldetector import UniversalDetector

app = Flask(__name__)

@app.route('/')
def index():
    name = "helo"
    return render_template('index.html', title='index', name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # ファイルがアップロードされた場合
        if 'file' not in request.files:
            return render_template('upload.html', message='ファイルを選択してください')

        file = request.files['file']

        # ファイルが空の場合
        if file.filename == '':
            return render_template('upload.html', message='ファイルが選択されていません')

         # アップロードされたファイルのファイル名を取得
        uploaded_filename = file.filename
        # ファイル名と拡張子を分離
        file_name, file_extension = os.path.splitext(uploaded_filename)
        
        
        # アップロードされたCSVファイルの文字コードを検出
        file_contents = file.read()
        detector = UniversalDetector()
        for line in file_contents :
            detector.feed(line)
            if detector.done : break
        detector.close()

        csv_encoding = detector.result['encoding']
        if csv_encoding == 'SHIFT_JIS' :
            csv_encoding = 'CP932'
        print(csv_encoding)

        # CSVを文字コードを指定して読み込み、Hyperファイルに変換
        df = pd.read_csv(io.BytesIO(file_contents))
        # hyper作成
        hyper_bytes = pantab.frame_to_hyper(df, f'{file_name}hyper',table='table')

        # ダウンロード
        downloaded_filename = 'converted.hyper'
        response = Response(
            hyper_bytes,
            content_type='application/octet-stream')
        response.headers['Content-Disposition'] = f'attachment; filename={downloaded_filename}'
        return response

    return render_template('upload.html', message='')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)  






