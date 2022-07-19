# Templates

## PySpark

Libraries you'll need when working in pyspark.
Important to use f as otherwise you can redefine in-built python functions such as max, min

    import pyspark.sql.functions as f
    from pyspark.sql.window import Window

    
Splitting a string (scan): 
    df.withColumn(f.split(f.col('column_name'), delimiter)[position])
