from statsmodels.tsa.exponential_smoothing.ets import ETSModel


class ForecastingModel:
    
    def __init__(self, error, trend, seasonal, damped_trend, seasonal_periods, initialization_method):
        self.model = None
        self.error = error
        self.trend = trend
        self.seasonal = seasonal
        self.damped_trend = damped_trend
        self.seasonal_periods = seasonal_periods
        self.initialization_method = initialization_method
    
    def initialize_model(self, dataset):
        self.model = ETSModel(
            endog=dataset,
            error=self.error,
            trend=self.trend,
            seasonal=self.seasonal,
            damped_trend=self.damped_trend,
            seasonal_periods=self.seasonal_periods,
            initialization_method=self.initialization_method
        )
    
    def fit(self, dataset):
        if not self.model:
            self.initialize_model(dataset)

        fitted_model = self.model.fit(maxiter=1000)
        return fitted_model