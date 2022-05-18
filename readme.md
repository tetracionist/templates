# Templates

## PySpark

It's good practice to include the functions that you need rather than the entire functions library

    from pyspark.sql.functions import col
    from pyspark.sql.functions import coalesce, split
    from pyspark.sql.functions to_timestamp, to_date, date_format
