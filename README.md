# 話者認識音声操作ロボット「クルックー」

発表時の動画
https://youtu.be/aK80Cryjd7w

【使用方法】
RaspberryPiにproject/robotフォルダをコピーする
音声認識はJulius(https://julius.osdn.jp/)に辞書登録をしている
juliusデータは重いので別途アップ

【データ構成】
├── README.md
├── createmodel    # モデル作成用
│   ├── create_model.ipynb     # モデル作成用
│   ├── create_model_noise.ipynb    # ノイズをMFCCで削除する手法
│   ├── kenshou.ipynb    # パラメータ毎の比較検証結果
│   ├── sound    # 学習用音声ファイル
│   └── validation.ipynb    # テストデータ検証用ファイル
└── project
    └── robot    # RaspberryPiにコピー
        ├── audio    # 話者認識結果により再生される音声ファイル
        │   ├── arisa.wav
        │   ├── endo.wav
        │   └── takahashi.wav
        ├── led.py
        ├── main.py
        ├── model    # 学習済みモデル
        │   ├── model_RBF.sav
        │   └── s_scaler.sav
        ├── model.py
        ├── model_noise.py
        ├── motor.py
        └── wav   # wav出力フォルダ
