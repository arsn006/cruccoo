# -*- coding: utf-8 -*-

import glob
import os
import numpy as np
import librosa
import librosa.display
import pickle
from sklearn.preprocessing import StandardScaler
import time
import subprocess

MODEL_PATH = "./model/model_RBF.sav"    # 学習済みモデル
SS_MODEL_PATH = "./model/s_scaler.sav"    # StandardScaler
A_WAV = "aplay ./audio/arisa.wav"
K_WAV = "aplay ./audio/k.wav"
E_WAV = "aplay ./audio/endo.wav"
T_WAV = "aplay ./audio/takahashi.wav"
class Predict_SVM:
    def predict(self):
        files = glob.glob("./wav/*wav")
        wav_path = max(files, key=os.path.getctime)
        print("wav_path", wav_path)

        y, sr = librosa.load(wav_path, sr=4096)    # 約4kHzでリサンプリングして読み込む
        mfccs = librosa.feature.mfcc(y, sr=sr, n_mfcc=100)
        x_test = mfccs.mean(axis=1)
        x_test = x_test[np.newaxis]
        ss_loaded_model = pickle.load(open(SS_MODEL_PATH, "rb"))
        x_test_std = ss_loaded_model.transform(x_test)

        loaded_model = pickle.load(open(MODEL_PATH, "rb"))
        y = loaded_model.predict(x_test_std)
        print("y", y)

        if y == 0:
            subprocess.call(A_WAV, shell=True)
            time.sleep(3)
        elif y == 1:
            subprocess.call(K_WAV, shell=True)
            time.sleep(3)
        elif y == 2:
            subprocess.call(E_WAV, shell=True)
            time.sleep(3)
        else:
            subprocess.call(T_WAV, shell=True)
            time.sleep(3)
        

        # wavを全て削除
        for filename in  files:
            os.remove(filename)
