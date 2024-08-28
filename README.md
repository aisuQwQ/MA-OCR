# MA-OCR
フルスクリーンゲームの翻訳機<br>
OCRで文字認識、DeepLで翻訳、tkinterでオーバーレイ表示<br>

## 使い方
sample-setting.pyを編集し、ファイル名をsetting.pyにする

### 変数名
API_KEY:string DeepL apiのAPIKEY<br>
source_lang:string 翻訳元の言語<br>
target_lang:string 翻訳先の言語<br>
OCR_KEY:string OCRを起動するキー<br>
DEL_KEYstring 翻訳結果を画面から消すキー<br>

## おまけ
翻訳はキャッシュされる<br>
mydic.pyを編集・実行して翻訳辞書をカスタマイズ