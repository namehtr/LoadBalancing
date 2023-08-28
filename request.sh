#!/bin/bash

echo "Starting requests at: $(date)"

for i in {1..10000}
do
   curl -X POST http://localhost
done

echo "Finished requests at: $(date)"