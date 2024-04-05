# import pandas as pd
# import pyspark.pandas as ps
#
# import pandera as pa
#
# from pandera.typing.pyspark import DataFrame, Series

from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()



# class Schema(pa.DataFrameModel):
#     state: Series[str]
#     city: Series[str]
#     price: Series[int] = pa.Field(in_range={"min_value": 5, "max_value": 20})


# create a pyspark.pandas dataframe that's validated on object initialization
df = spark.createDataFrame(
    {
        'state': ['FL','FL','FL','CA','CA','CA'],
        'city': [
            'Orlando',
            'Miami',
            'Tampa',
            'San Francisco',
            'Los Angeles',
            'San Diego',
        ],
        'price': [8, 12, 10, 16, 20, 18],
    }
)
print(df)