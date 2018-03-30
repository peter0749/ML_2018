## HW1 README
Author: 404410030 資工三 鄭光宇

#### 套件需求

```
python >= 2.7
jupyter
numpy
scikit-image
tqdm
matplotlib
```

#### 如何執行
1. 將 E-course 上 `CroppedYale.7z` 壓縮檔解壓縮到與 `NN.ipynb` 同目錄下，並確保解壓出來的 `./CroppedYale` 目錄下有人臉種類 label 相對應的所有子目錄。
2. 開啟這個作業的 jupyter notebook，也就是 `NN.ipynb`:
    ```bash
    jupyter notebook NN.ipynb
    ```
    
    jupyter notebook 開啟後，按下 `RUN`
    
    會跑出 SAD, SSD 使用 Nearest Neighbor 方法分類人臉的 Accuracy。

