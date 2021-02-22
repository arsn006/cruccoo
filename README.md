# 話者認識音声操作ロボット「クルックー」

## 発表時の動画
https://youtu.be/aK80Cryjd7w

## 【使用方法】
- RaspberryPiにproject/robotフォルダ以下をコピーする
- 音声認識部分はJulius( https://julius.osdn.jp/ )に辞書登録をしています
- juliusデータは重いので別途アップ

## 【データ構成】
├── README.md<br>
├── createmodel    # モデル作成用<br>
│   ├── create_model.ipynb     # モデル作成用<br>
│   ├── create_model_noise.ipynb    # ノイズをMFCCで削除する手法<br>
│   ├── kenshou.ipynb    # パラメータ毎の比較検証結果<br>
│   ├── sound    # 学習用音声ファイル<br>
│   └── validation.ipynb    # テストデータ検証用ファイル<br>
└── project<br>
    └── robot    # RaspberryPiにコピー<br>
        ├── audio    # 話者認識結果により再生される音声ファイル<br>
        │   ├── arisa.wav<br>
        │   ├── endo.wav<br>
        │   └── takahashi.wav<br>
        ├── led.py<br>
        ├── main.py<br>
        ├── model    # 学習済みモデル<br>
        │   ├── model_RBF.sav<br>
        │   └── s_scaler.sav<br>
        ├── model.py<br>
        ├── model_noise.py<br>
        ├── motor.py<br>
        └── wav   # wav出力フォルダ<br>
