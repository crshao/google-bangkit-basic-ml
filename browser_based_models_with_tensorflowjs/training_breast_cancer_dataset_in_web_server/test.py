import csv

# To find out number of features
reader = csv.reader(open('browser_based_models_with_tensorflowjs/training_breast_cancer_dataset_in_web_server/wdbc-test.csv'))
print(len(next(reader)))

# 31 label included, so 30 is the number of features