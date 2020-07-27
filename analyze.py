#! /usr/bin/env python

import sys
import json
import csv

def load_file(fn):
    with open(fn, 'r') as f:
        return json.loads(f.read())

def analyze(j):
    print(len(j))

    out_rows = []
    for info in j:
        instance_type = info['instance_type']
        try:
            on_demand = info['pricing']['us-east-1']['linux']['ondemand']
            # This is a dict
            reserved = info['pricing']['us-east-1']['linux']['reserved']

            reserved['instance_type'] = instance_type
            reserved['on_demand'] = on_demand

            out_rows.append(reserved)
        except Exception as e:
            print('Failed to parse', instance_type)

    return out_rows

def write_csv(fn, rows):
    with open(fn, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    fn_in = sys.argv[1]
    fn_out = sys.argv[2]

    j = load_file(fn_in)
    out = analyze(j)
    write_csv(fn_out, out)
