from abc import ABC, abstractmethod
from ..shared.static_variables import GRIDSEARCH_CV_NUM_PARALLEL_JOBS
class MleapEstimator(ABC):

    def __init__(self, 
                verbose=0, 
                n_jobs=GRIDSEARCH_CV_NUM_PARALLEL_JOBS,
                num_cv_folds=3, 
                refit=True):
        self._num_cv_folds=num_cv_folds
        self._verbose=verbose
        self._n_jobs=n_jobs
        self._refit=refit

    @abstractmethod
    def build(self):
        """ Returns the estimator and its hyper parameters"""
    
    @abstractmethod
    def save(self):
        """ saves the trained model to disk """
    @abstractmethod
    def get_estimator_name(self):
        """ returs the name of the estimator"""    

    def set_trained_model(self, trained_model):
        self._trained_model = trained_model
    
    def get_trained_model(self):
        return self._trained_model