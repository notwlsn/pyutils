import pandas as pd
import numpy as np
import glob
import time
start = time.time()

print("reading...")

all_data = pd.DataFrame()
for f in glob.glob("*.xlsx"):
   df = pd.read_excel(f)
   all_data = all_data.append(df, ignore_index=True)

print("writing...")

#save as a new data frame
writer = pd.ExcelWriter('mycollected_data.xlsx', engine='xlsxwriter')
all_data.to_excel(writer, sheet_name='Sheet1')
writer.save()

print("success.")
end = time.time()
print(end - start)
