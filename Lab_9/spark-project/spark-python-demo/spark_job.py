from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def read_file(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def transform_data(df):
    return df.select([col for col in df.columns if dict(df.dtypes)[col] in ('int', 'double')])

def write_file(df, output_path):
    df.write.mode("overwrite").parquet(output_path)

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Spark Python Demo") \
        .getOrCreate()

    input_path = "sample.csv"
    output_path = "output_parquet"

    df = read_file(spark, input_path)
    transformed_df = transform_data(df)
    write_file(transformed_df, output_path)

    spark.stop()
