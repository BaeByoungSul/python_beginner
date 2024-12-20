## Python Machine Learn Tutorial

1. Import the data
2. Clean the data
3. Split the data into training / test sets
4. Create a model
5. Train the model
6. Make predictions
7. Evaluate and Improve

## Libraries

- Numpy
- Pandas
- MatPlotLib
- Scikit-Learn

## Tool

> > - 아나콘다(Anaconda)란?  
> >   아나콘다는 머신러닝이나 데이터 분석 등에 사용하는 여러가지 패키지가 기본적으로 포함되어있는 파이썬 배포판입니다.

> > - 아나콘다 설치 : Python, Jupyter Notebook 포함되어 있음
> >   https://www.anaconda.com/download

> > - Jupyter Notebook  
> >   Jupyter에서 제작한 웹 기반[1] 인터랙티브 컴퓨팅 플랫폼이다. Jupyter의 이름은 주피터가 지원하는 세 개의 핵심 언어인 Julia, Python 그리고 R에서 유래했으며, 목성의 위성의 발견이 기록된 갈릴레오 갈릴레이의 공책에 대한 존경의 의미도 갖는다고 한다

## Hello world

> > - Jupyter Notebook 실행: 명령창에서 jupyter notebook
> > - Create notebook : Files 탭 >> New >> Python 3

```
print('Hello world')
```

## Import dataset

> > -. Download : https://www.kaggle.com/ : video game sales or GregorySmith

```
import pandas as pd
df = pd.read_csv('vgsales.csv')
df.shape

df.describe()

```

## Predict music genre

> > download music.csv : https://github.com/mosh-hamedani/python-supplementary-materials

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data= pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
# model.fit(X, y) #Here x includes the dataframe with headers
model.fit(X.values, y) #Here x.values will have only values without headers
predictions = model.predict([[21, 1], [22,0] ])
predictions
```

> > Caculate accuracy score(music)
> > Persisting Models(music_2)
> > Visualizing a Decision Tree (visualiz_decision)

- jupyter notebook실행 후 vs code에서 확인
- Install Graphviz (dot) Stephanvs
- Install Graphviz Interactive Preview

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
music_data= pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()
model.fit(X.values, y) #Here x includes the dataframe with headers

tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age', 'gender' ] ,
                     class_names= sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True    )


```

```
import pandas as pd

df = pd.DataFrame()
df['키'] = [170, 144, 156, 177, 181, 188, 181, 161]
df['체중'] = [55, 52, 60, 77, 65, 89, 90, 60]

df['키'].mean() # 평균
df['키'].median() # 중앙값 = df['키'].quantile(0.5)
df['키'].mode() # 최빈값
df['키'].std() # 표준 편차
df['키'].var() # 표본 분산
df['키'].sum() # 합계
df['키'].min() # 최소값
df['키'].max() # 최대값
df['키'].max()-df['키'].min() # 범위
df['키'].nunique() # 유니크한 원소 개수
df['키'].quantile(0.25) # 제 1 사분위수
df['키'].quantile(0.75) # 제 2 사분위수
df['키'].quantile(0.75) - df['키'].quantile(0.25) # 사분위 범위
df['키'].kurtosis() # 첨도
df['키'].skew() # 왜도
df['키'].cov(df['체중']) # 공분산
df['키'].corr(df['체중']) # 상관계수
```

## Shortcut in jupyter

- green bar : edit mode
- blue bar : command mode >> Ctrl + Shift + H
- insert and cell : command mode >> select cell and type a or b ( above, below )
- delete cell : type d twice
- run button : only selected cell run
- menu : Run >> Run All Cells
- show method and attributes : type df dot and tab
- To see the tooltip of method: shift + tab
- comment line : ctrl + slash ( / )

https://www.youtube.com/watch?v=7eh4d6sabA0

# Emphasis

This is _Italic_.  
This is **Bold**  
This one is **_Bold and Italic_**.

# Blockquotes.

> Lev 1.  
> Lev 1, Continue.
>
> > Lev 2.  
> > Lev 2, Continue.
> >
> > > Lev 3

# Ordered Lists and Unordered Lists

1. 내 이름은 박병
2. 내 이름은 TH
3. 내 이름은 TS

- 기호로 -, \*, + 를 사용할 수 있다.
  - 2단계
    - 3단계

# Code Blocks

Code 를 보이려면 이렇게 합니다. <!-- 4칸 띄우기 또는 Tab-->

    import pandas as pd
    pd.killTH()

Like this..

# Image

![대체텍스트](./펭귄.jpg)

## 라인 긋기 ( 3 dash)

- This is a bullet point

* this is also a bullet point

---

This code is test python code

```python
date1 = now.strftime("%Y-%m-%d %H:%M:%S")
print( date1 )
date1 = now.strftime("%Y-%m-%d %p %I:%M:%S %a %b %A %B ")
print( date1 )
```

---

### [Link to kolon iken ](https://iken.kolon.com)

---

## ![Image Link](https://github.com/BaeByoungSul/python_beginner/blob/main/apartment_view.jpg)

---

## python_beginner

### python_beginner

#### python_beginner
