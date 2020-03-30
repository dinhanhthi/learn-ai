import pandas as pd
import numpy as np
from sklearn.cluster import MeanShift

from popai.lib.helpers_timestamps import set_index

from popai.processings.BaseProcessing import BaseProcessing

class WindowDetection(BaseProcessing):
    """
    Detecting and separating a time-series data into windows of time.

    Data will be resampled to the most popular step before performing the detection.

    Attributes
    ----------

    dict_report: dict
        The dictionary that contain the report.

    col_time: str
        The column that contains datetime information. If set to `'index'`, the 
        datetime column is the index of the dataframe.

    gap: DateOffset, Timedelta, str or 'auto', default='auto'.
        The minimum value of gaps used to detect windows.

        'auto':  the minimum of gaps is determined automatically based on Mean-Shift clustering. 
        First, we find all difference of two timestamps. Second, Mean-Shift will help use find the 
        suddenly increasing gap between timestamps.

    resample_how: function
        Method for down/re-sampling, default to np.mean for downsampling.
        You can use (with caution!) other numpy/self-defined functions 
        (e.g. `np.max, `np.min`, np.sum`) for this.
    """
    
    def __init__(self, col_time='index', gap='auto', resample_how=np.mean):
        """
        Instantiate the class.

        Parameters
        ----------

        col_time: str
        The column that contains datetime information. If set to `'index'`, the 
        datetime column is the index of the dataframe.

        gap: DateOffset, Timedelta, str or 'auto', default='auto'.
            The minimum value of gaps used to detect windows.

            'auto':  the minimum of gaps is determined automatically based on Mean-Shift clustering. 
            First, we find all difference of two timestamps. Second, Mean-Shift will help use find the 
            suddenly increasing gap between timestamps.

        resample_how: function
            Method for down/re-sampling, default to np.mean for downsampling.
            You can use (with caution!) other numpy/self-defined functions 
            (e.g. `np.max, `np.min`, np.sum`) for this.
        """
        
        super().__init__()
        self.col_time = col_time
        self.gap = gap
        self.resample_how = resample_how
        if resample_how.__name__:
            self.dict_report['resample_how'] = resample_how.__name__
        
        
    def _find_gap_auto(self, df):
        """
        Automatically finding the gap in a time-series dataframe.
        """
        
        X = df[self.col_time].diff().unique()
        X.sort()
        X = X[1:].reshape(-1,1) # don't forget to remove NaN at the beginning
        
        clustering = MeanShift().fit(X)
        labels = clustering.labels_
        gap = pd.to_timedelta((X[labels!=0].min() + X[labels==0].max())/2)
        
        return gap
    
    
    def run(self, data):
        """

        Parameters
        ----------
        data: pd.DataFrame or pd.Series
            The data to transform.
        
        Returns
        -------
        pd.DataFrame
            The transformed data.
        """
        
        # make sure dataframe has a separated datetime column
        df_tmp = set_index(data, self.col_time)
        self.col_time = df_tmp.index.name
        df_tmp = df_tmp.reset_index()
        print('col_time: ', self.col_time)
        
        # check the regularity of the data (already resampled?)
        is_regular = (df_tmp[self.col_time].diff().value_counts().shape[0] == 1)
        if not is_regular:
            most_period = df_tmp[self.col_time].diff().value_counts().index[0]
            self.dict_report['resample_rule_auto'] = most_period
            df_tmp = df_tmp.resample(rule=most_period, on=self.col_time).apply(self.resample_how)
            df_tmp.dropna(inplace=True)
            df_tmp = df_tmp.reset_index()
        
        
        if self.gap == 'auto':
            self.gap = self._find_gap_auto(df_tmp)
        self.dict_report['gap used'] = self.gap
        
        df_0 = df_tmp[self.col_time].diff()
        
        w_starts = df_tmp[~(df_0 < pd.to_timedelta(self.gap))].index
        w_ends = (w_starts[1:] - 1).append(pd.Index([data.shape[0]-1]))
        
        self.dict_report['number_of_windows'] = len(w_starts)

        w_idx = 0
        for i in range(w_starts.shape[0]):
            df_tmp.loc[w_starts[i]:(w_ends[i]+1), 'window'] = w_idx
            w_idx += 1

        df_tmp.window = df_tmp.window.astype(int)
        
        return df_tmp