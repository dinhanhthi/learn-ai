# Le test de biblios de Dataswati

- Candidature: **Anh-Thi Dinh**.
- Email: **dinhanhthi@gmail.com**.
- Date: **19-11-19**
- Subjet:  **Des représentations de séries temporelles** 

*J'utilise l'anglais pour rédiger ce rapport en raison de son adéquation aux concepts de Machine Learning et de Data Science.  En fait, c'est plus facile pour moi dans un court laps de temps comme celui-ci.* 

---

Below are the state of the art about Time Series tasks and Time Series Representations.

[TOC]

## 1. Overview Time Series (TS) Tasks

### 1.1. TS Mining fields

Discover (automatically) meaningful knowledge from TS. Sometimes, some tasks can perform predictions.

- **Motif discovery**: motif is a part or subsequence of TS with specific properties. Discovery a motif is to find (in TS) (some) motifs. There are some types of motifs:
  - *Recurrent motif*: motif appear recurrently without overlap.
  - *Infrequent or surprising motif & anomaly detection*: motif has never been seen or has low  frequency of occurrence. 
  - *Task-specific relevant motif*:  Motif discovery can be driven with a specific task in mind. E.g. TS *shapelet*.
- **TS retrieval**:  Given a query time series, time series retrieval aims to find the most similar time
  series in a dataset based on their information content. This is *the most of the research attention* in time series mining
  - *Issue*: the computational complexity. 
  - *Solution*: Reduce dimensionality of TS + Approximate similarity measures + Efficient
    indexing.
- **Clustering**:  aims to find groups of similar time series in a dataset.
  - *Issue*: determine the number of clusters + understand the meaning of clusters.
  - 2 types: *whole sequence* + *subsequence* $\to$ take whole/sub to perform the clustering.
    - Be careful on the extracting process because of meaningless subs.
  - It can be a stage for other tasks (summarization, motif discovery).
- **Temporal pattern mining - Rule discovery**: aims to relate patterns in a time series to other patterns from the same time series or others.
  - *Approach*: discretize TS into sequences of symbols and find the relationship between symbols.
  - *Methods*: association rules, decision tree.
- **Anormaly detection**: detecting "patterns in data that do not conform to expected behavior". 
  - *Approaches*: abnormal motif discovery / difference of a point to the median of the other points in its neighborhood. 
- **Summarization**: automatic summary may be useful to get insights on the "long and complex" TS.
  - *Approaches*: using anormaly detection / motif discovery $\to$ report abnormal sequences; using clustering $\to$ get info from each cluster.
- **Classification**: predict a label given a time series in input of a model.
  - *Usage*s: patern recognition, spam filtering, medical diagnosis, anormaly detection, transaction sequence data in a bank or detecting malfunction in industry applications.
  - 2 types: *weak classification* (one single global label assigned), *strong classification* (sequence of labels assigned).

### 1.2. TS Analysis

It aims to develop techniques to analyze and model the temporal structure of time series to describe an underlying phenomena and possibly to forecast future values. The correlation of successive points in a time series is assumed.

### 1.3. Signal Processing

Broad field with many *objectives*: improve signal quality, to compress for storage / transmission, detect a particular pattern.

## 2. TS representations

A *TS representation* transforms a time series into another time series or a feature vector. *Objectives*: highlight relevant infos / remove noise / handle distortions / reduce dimensionality $\to$ decrease complexity for futur computations.

There may be <u>3 groups</u> based:

1. **Time-based representations**: produces a TS from a whole raw TS, i.e. $\Phi(T_n) = \hat{T}_n$. Make a lower dimensional space to speed up the computation.
2. **Feature-based representaions**: produces a scalar / set of scalars from a raw TS, i.e. $\Phi(T_n)=x_{\Phi(T_n)}$. E.g. Description of global distribution of values, global trends, global frequency content.
3. **Motif-based representations**: prodices a subsequence of a TS from a raw TS based on desired properties, i.e. $\Phi(T_n)=\hat{T}_n$.

### 2.1. Time-based representations

#### 2.1.1. Piecewise representations

TS is *segmented* then a *local feature* is computed for each segment (for eg. the mean, average rate of variations or a regression coefficient).

- <u>The segmentation process</u>: there are *adaptive* and *non-adaptive* segmentation techniques.
- <u>The representation of each segment</u>: which feature or set of features is extracted to represent each segment. 

Some techniques:

- **Sub-sampling**: One value is conserved every $h$ points of the time series. Mainly used in signal processing when a continuous signal has to be converted into a discrete one. 

  - <u>*Pros*</u>: faster computations + less storage requirements + easy to implement.
  - <u>*Cons*</u>: distortion of the time series shape.

  ```python
  # check the notebook 'test_biblios_python_thi.ipynb' for a full version
  def sub_sampling(signal, h):
      h = int(h) # to be sure that h is an integer number
      len_sig = signal.shape[0]
      new_signal = np.copy(signal)
      n_segments = len_sig // h
      for i in range(n_segments):
          new_signal[i*h:(i+1)*h] = signal[random.randint(i*h, (i+1)*h)]
      new_signal[n_segments*h:len_sig] = signal[random.randint(n_segments*h, len_sig-1)]
      return new_signal
  ```

- **PAA** (*Piecewise Aggregate Approximation*):  the *most important* time-based representation based on non-adaptive segmentation. Almost the same as *sub-sampling* except that the conserved value in this case is the *mean* of that segment. TS is segmented to $N$-fixed length segments.

  - <u>*Pros*</u>: higher fidelity in the representation of each segment + pros of *sub-sampling*.
  - <u>*Cons*</u>: mean is not always best (*solution*: add slope info / variance to mean, use SSV) + not good resolution of info (*solution*: use MPAA version).
  - <u>*Code*</u>: Use `from tslearn.piecewise import PiecewiseAggregateApproximation` [[ref]( https://tslearn.readthedocs.io/en/latest/gen_modules/piecewise/tslearn.piecewise.PiecewiseAggregateApproximation.html)] or using my below implementation.

  ```python
  # check the notebook 'test_biblios_python_thi.ipynb' for a full version
  def PAA(signal, N): # N fixed-length segment
      N = int(N) # to be sure that N is an integer number
      len_sig = signal.shape[0]
      new_signal = np.copy(signal)
      n_points = len_sig // N # number of points in each segment
      for i in range(N):
          new_signal[i*n_points:(i+1)*n_points] = np.mean(signal[i*n_points:(i+1)*n_points])
      new_signal[N*n_points:len_sig] = np.mean(signal[N*n_points:len_sig])
      return new_signal
  ```

- **APCA** (*Adaptive Piecewise Constant Approximation*): above *non-adaptive* segmentations have a weakness in that segments with constant values has the same resolution as the ones with fluctuations. APCA overcomes this cons by making segment length fitted to the shape of series and split into two smaller segments such as the division
  maximizes the variance reduction.

  - <u>*Implementation*</u>: the idea can be borrowed from [here](https://github.com/octavian-h/time-series-math/blob/master/src/main/java/ro/hasna/ts/math/representation/AdaptivePiecewiseConstantApproximation.java) (written in java), later work!

- **PLA** (*Piecewise Linear Approximation*): represent a TS by successive straight lines to model the shape of the TS. Straight lines? $\leftarrow$ interpolation / regression. 

  - *<u>Implementation</u>*: can be performed using `np.piecewise` or [pwlf](https://github.com/cjekel/piecewise_linear_fit_py) or [[1]](http://home.cse.ust.hk/~yike/icde15.pdf), below is an example of my idea.
  - *<u>Several variations</u>*: *Piecewise Linear Representation* (PLR), *Perceptually Important Point* (PIP), 
  
  ```python
  # interpolation:
  # check the notebook 'test_biblios_python_thi.ipynb' for a full version
  from scipy.interpolate import interp1d
  def PLA(signal, n_segments):
      len_sig = signal.shape[0]
      x = np.arange(1, len_sig+1)
      y = signal
      f = interp1d(x, y)
      n_points = len_sig // n_segments
      xnew = np.arange(0, len_sig, n_points)
      xnew[0] = 1
      xnew = np.append(xnew, len_sig)
      return xnew, f(xnew)
  ```

#### 2.1.2. Symbolic representations

TS is segmented and then discretized. A dictionary of symbols is either learned or applied in order to convert the time series into a series of symbols.

- <u>*Pros*</u>: we could take advantage of a wealth of techniques from the very mature field of string processing (text retrieval or bioinformatics fields). 
- <u>*Cons*</u>: don't support Euclidean queries + how we discretize TS (values, shape, slope)? How big of an alphabet?...

Some techniques:

- **SAX** (*Symbolic Aggregate approXimation*): relies on the *PAA* to produce symbolic sequences. It converts a TS into a sequence of symbols of length $N$.  The alphabet of symbols has a length $a > 2; a\in[1,\ldots,N]$.  
  - <u>*Usage & Pros*</u>: motif discovery, encoding TS + efficiently localized recurrent patterns.
  - *<u>Cons</u>*: choice of $N$ and $a$ (too small $\to$ noise, too big $\to$ miss shapes/trends of TS)
  - *<u>Code</u>*: Use `from tslearn.piecewise import SymbolicAggregateApproximation` [[ref](https://tslearn.readthedocs.io/en/latest/gen_modules/piecewise/tslearn.piecewise.SymbolicAggregateApproximation.html)] (check `test_biblios_python_thi.ipynb` for an example)

#### 2.1.3. Transform-based representation

TS is converted from the time domain into another domain (for eg. the time-frequency domain thanks to a wavelet transform).

- <u>*Some techniques*</u>: *filters*, *Discrete Wavelet Transform* (DWT), *Empirical Mode Decomposition* (EMD).
- <u>*Pros*</u>: useful to preprocess the raw TS + remove noise + gain access to relevant shapes of TS + reduce dinensionality + extract global trend from raw TS.  
- *<u>Code</u>*: Use `import pywt` [[ref](https://pywavelets.readthedocs.io/en/latest/)]

### 2.2. Feature-based representations

- *<u>Suited for</u>*: classical ML algorithms.
- *<u>Issue</u>*: which type of features is relevant to represent TS of dataset? $\to$ *solution*: extract a very large set of distinct features and then select the relevant ones.
- *<u>Example</u>*: [3]

### 2.3. Motif-based representations

Three main types of motifs: *recurrent motif*, *infrequent or surprising motifs* and *discriminant motifs*. 

- **Recurrent motif**: motif appear recurrently without overlap. A *match* is defined as a distance between two subsequences lower than an arbitrary threshold. 
- **Surprising motif**: a motif whose frequency of occurrence significantly differs from that expected by chance 
- **Discrininant motifs**: motifs whose frequency of occurrence in the time series depends on the time series class label.  It's useful to perform time series classification. $\to$ *approach*: TS *shapelet*.
  - *<u>Code</u>*: Using `tslearn.shapelets.ShapeletModel` [[ref](https://tslearn.readthedocs.io/en/latest/gen_modules/shapelets/tslearn.shapelets.ShapeletModel.html)].

Some types:

- **Matrix profile**: is composed of 2 arrays: *distance* and *1-NN indices*. Large distances are anomalous events. Repeated paterns are found in the 1-NN indices.
  - *<u>Pros</u>*:  it is domain agnostic, fast, provides an exact solution (approximate when desired) and only requires a single parameter. 
  - *<u>Algorithms</u>*: STAMP, STOMP, SCRIMP++.
  - *<u>Code</u>*: `pip install matrixprofile-ts` [[ref](https://pypi.org/project/matrixprofile-ts/)]
  - *<u>Example</u>*: [this notebook](https://github.com/matrix-profile-foundation/article-matrix-profile-intro/blob/master/Matrix%20Profile%20Example.ipynb).

## 3. Distance mesures

A *distance measure* measures the similarity between TSs based on raw TSs or their representations.

- **Lock-step distances**: the i^th^ point of TS is compared to i^th^ point of another TS.
  - ***Euclidean distance***: $d(T_1, T_2)_{L^2} = \sum_{i=1}^L \sqrt{(T_1(i) - T_2(i))^2}$. <u>Cons</u>: sensitivity to distortions / difficult to work with TS of various lenghts.
- **Elastic distances**: compare one point of this TS to several points of another TS $\to$ handle distortions.
  - ***Dynamic Time Warping*** (DTW): finding the best possible alignment between two TSs. <u>Cons</u>: its scalability + complexity.
- **Edit distances**: quantify similarity of two sequences of symbols (evaluate the cost to transform one sequence to the other, by counting the minimum number of operations required ). <u>Drawback</u>: TS need to be transformed to symbolic representation. <u>Example</u>: LCSS, EDR.

$\Rightarrow$ Check the difference between Euclidean and DTW in [[2]](http://www.cs.ucr.edu/~eamonn/sdm-02.pdf).

## 4. Apply Ml algorithms on TS

2 approaches: *time-based* and *feature-based*.

- **Time-based**: consider the whole time series and apply *distance measures* on TS to quantify their similarity.
- **Feature-based**: transform the time series into a vector of features.

## 6. Distortions

- **Amplitude distortions** $\to$ *solution*: transformation of the time series, e.g. z-normalization, SSV.
- **Time-warping distortions** $\to$ more difficult $\to$ using *elastic distances*.

## Bibliography

[1] **Luo, Ge, et al**. "*Piecewise linear approximation of streaming time series data with max-error guarantees*." *2015 IEEE 31st International Conference on Data Engineering*. IEEE, 2015. 

[2] **Chu, Selina, et al.** "*Iterative deepening dynamic time warping for time series*." *Proceedings of the 2002 SIAM International Conference on Data Mining*. Society for Industrial and Applied Mathematics, 2002. 

[3] **Fulcher, Ben D., and Nick S. Jones**. "Highly comparative feature-based time-series classification." *IEEE Transactions on Knowledge and Data Engineering* 26.12 (2014): 3026-3037. 