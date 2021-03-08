# 話者認識音声操作ロボット「クルックー」

## 「クルックー」操作動画
https://youtu.be/aK80Cryjd7w

## 仕様
- モーターで動くプラモデルを、RaspberryPiで制御しています。
- 「前に進め」、「後ろに下がれ」、「右に曲がれ」、「左に曲がれ」、「全体止まれ」と声をかけて操作します。
- 「クルックーおいで」と声をかけると、話者を認識し声をかけた相手に合わせて応答します。<br>
例）Aさんが声をかけると「ありさ、どこー？」と応答して前進、Bさんが声をかけると「よったん、どこいるの？」と応答して前進します。

## 制作期間
- 10日間
- 買い出し、プラモデル組み立て、環境構築：5日
- 実装：5日

## 感想
最初に作りたいものを決め、そこから必要な技術を洗い出し、実装していったので初めて扱う技術が多く<br>
道具やパーツの買い忘れや、はんだ付けが上手くいかず接触不良でセンサーが動かないなど、苦労した点も多かったが<br>
後半の実装部分では、没頭して作業に打ち込むことができ、どんどん完成形へと近づいて行く工程がとても楽しかった。<br>
制作進行の経験から、最初にガントチャートを作成し、進捗具合を見ながら仕様変更など柔軟に対応することで、発表時に動くものを見ていただけた。

## 今後実装したい機能
- 話者認識を間違えた時には、オンライン学習（逐次学習）できる機能
- 話者に向かって進む機能

## 【使用方法】
- RaspberryPiにproject/robotフォルダ以下をhome/pi/にコピーする
- Juliusデータをhome/pi/にコピーする
音声認識部分はJulius( https://julius.osdn.jp/ )に辞書登録をしています（juliusデータは重いので別途アップ）
- ターミナルでコマンド実行　julius -C ~/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -rejectshort 1000 -gram ~/julius/control/control -input mic -module -record ~/robot/wav/
- ターミナルをもう一つ立ち上げ、コマンド実行　python main.py

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
