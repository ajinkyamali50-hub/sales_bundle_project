df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Workspace/SALES_BUNDLE_PROJECT/data/sales.csv")

display(df)