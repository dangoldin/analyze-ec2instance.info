# Analyze ec2instances.info

This script takes the result of the [https://github.com/powdahound/ec2instances.info](ec2instances.info) data and extracts the instance type, on demand cost, and reservation costs into a CSV file.

To run:

```
python3 analyze.py ../ec2instances.info/www/instances.json out.csv
```
