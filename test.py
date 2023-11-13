from neuralprophet import NeuralProphet

import pandas as pd


df_given = pd.read_csv('./data_given.csv')


m = NeuralProphet()
m.set_plotting_backend("plotly-static")  # show plots correctly in jupyter notebooks
metrics = m.fit(df_given)


df_future = m.make_future_dataframe(df_given, n_historic_predictions=True, periods=365)

# Predict the future
forecast = m.predict(df_future)

m.plot(forecast)