import numpy as np

# original data
marks=np.array([
    85,90,np.nan,70,95,
    -30,90,105,np.nan,80,
])

print("Original Data:",marks)

missing =np.sum(np.isnan(marks))
print("Missing Values:",missing)

average=np.nanmean(marks)
print("Average Marks:",average)

valid = marks[(marks >= 0) & (marks <= 100)]
print("\nValid Marks:")
print(valid)

# Step 5: Remove duplicate values
unique = np.unique(valid)
print("\nUnique Marks:")
print(unique)

# Step 6: Final analysis
print("\nFinal Average:", np.mean(unique))
print("Highest Marks:", np.max(unique))
print("Lowest Marks:", np.min(unique))