import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node aisles
aisles_node1773883930224 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://instacart-market/raw/instacart/aisles/"], "recurse": True}, transformation_ctx="aisles_node1773883930224")

# Script generated for node orders products
ordersproducts_node1773884440196 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://instacart-market/raw/instacart/order_products/"], "recurse": True}, transformation_ctx="ordersproducts_node1773884440196")

# Script generated for node orders
orders_node1773884391852 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://instacart-market/raw/instacart/orders/"], "recurse": True}, transformation_ctx="orders_node1773884391852")

# Script generated for node products
products_node1773883799479 = glueContext.create_dynamic_frame.from_catalog(database="instacart_market_db", table_name="products_raw", transformation_ctx="products_node1773883799479")

# Script generated for node departments
departments_node1773884578256 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://instacart-market/raw/instacart/departments/"], "recurse": True}, transformation_ctx="departments_node1773884578256")

# Script generated for node Change Aisles
ChangeAisles_node1773903183330 = ApplyMapping.apply(frame=aisles_node1773883930224, mappings=[("aisle_id", "string", "aisle_id", "int"), ("aisle", "string", "aisle", "string")], transformation_ctx="ChangeAisles_node1773903183330")

# Script generated for node Change OrdersProducts
ChangeOrdersProducts_node1773903187995 = ApplyMapping.apply(frame=ordersproducts_node1773884440196, mappings=[("order_id", "string", "order_id", "int"), ("product_id", "string", "product_id", "int"), ("add_to_cart_order", "string", "add_to_cart_order", "int"), ("reordered", "string", "reordered", "int")], transformation_ctx="ChangeOrdersProducts_node1773903187995")

# Script generated for node Change Orders
ChangeOrders_node1773903192636 = ApplyMapping.apply(frame=orders_node1773884391852, mappings=[("order_id", "string", "order_id", "int"), ("user_id", "string", "user_id", "int"), ("eval_set", "string", "eval_set", "string"), ("order_number", "string", "order_number", "int"), ("order_dow", "string", "order_dow", "int"), ("order_hour_of_day", "string", "order_hour_of_day", "int"), ("days_since_prior_order", "string", "days_since_prior_order", "int")], transformation_ctx="ChangeOrders_node1773903192636")

# Script generated for node Change Products
ChangeProducts_node1773903197936 = ApplyMapping.apply(frame=products_node1773883799479, mappings=[("product_id", "int", "product_id", "int"), ("product_name", "string", "product_name", "string"), ("aisle_id", "int", "aisle_id", "int"), ("department_id", "int", "department_id", "int")], transformation_ctx="ChangeProducts_node1773903197936")

# Script generated for node Change Department
ChangeDepartment_node1773903206106 = ApplyMapping.apply(frame=departments_node1773884578256, mappings=[("department_id", "string", "department_id", "int"), ("department", "string", "department", "string")], transformation_ctx="ChangeDepartment_node1773903206106")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeAisles_node1773903183330, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773902866795", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773903586108 = glueContext.write_dynamic_frame.from_options(frame=ChangeAisles_node1773903183330, connection_type="s3", format="glueparquet", connection_options={"path": "s3://instacart-market/processed/aisles/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1773903586108")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeOrdersProducts_node1773903187995, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773883772313", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773885900013 = glueContext.write_dynamic_frame.from_options(frame=ChangeOrdersProducts_node1773903187995, connection_type="s3", format="glueparquet", connection_options={"path": "s3://instacart-market/processed/order_products/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1773885900013")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeOrders_node1773903192636, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773902866795", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773903603432 = glueContext.write_dynamic_frame.from_options(frame=ChangeOrders_node1773903192636, connection_type="s3", format="glueparquet", connection_options={"path": "s3://instacart-market/processed/instacart_orders/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1773903603432")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeProducts_node1773903197936, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773902866795", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773903621986 = glueContext.write_dynamic_frame.from_options(frame=ChangeProducts_node1773903197936, connection_type="s3", format="glueparquet", connection_options={"path": "s3://instacart-market/processed/products/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1773903621986")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeDepartment_node1773903206106, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1773902866795", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1773903887516 = glueContext.write_dynamic_frame.from_options(frame=ChangeDepartment_node1773903206106, connection_type="s3", format="glueparquet", connection_options={"path": "s3://instacart-market/processed/departments/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1773903887516")

job.commit()