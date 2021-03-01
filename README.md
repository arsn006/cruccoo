# 話者認識音声操作ロボット「クルックー」

## 「クルックー」操作動画
https://youtu.be/aK80Cryjd7w

## 仕様
- 「前に進め」、「後ろに下がれ」、「右に曲がれ」、「左に曲がれ」、「全体止まれ」と声をかけて操作します。
- 「クルックーおいで」と声をかけると、話者を認識し声をかけた相手に合わせて応答します。
例）Aさんが声をかけると「ありさ、どこー？」と応答して前進、Bさんが声をかけると「よったん、どこいるの？」と応答して前進します。

## 今後実装したい機能
- 話者認識を間違えた時には、オンライン学習（逐次学習）できる機能
- 話者に向かって進む機能

## 【使用方法】
- RaspberryPiにproject/robotフォルダ以下をhome/pi/にコピーする
- Juliusデータをhome/pi/にコピーする
音声認識部分はJulius( https://julius.osdn.jp/ )に辞書登録をしています（juliusデータは重いので別途アップ）
- ターミナルでコマンド実行　julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -rejectshort 1000 -gram ~/julius/control/control -input mic -module -record ~/robot/wav/
- ターミナルをもう一つ立ち上げ、コマンド実装　python main.py

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
