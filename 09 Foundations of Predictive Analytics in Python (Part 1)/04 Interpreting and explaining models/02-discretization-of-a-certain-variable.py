# Discretize the variable time_since_last_donation in 10 bins
basetable["bins_recency"] = pd.qcut(basetable["time_since_last_donation"],10)

# Print the group sizes of the discretized variable
print(basetable.groupby("bins_recency").size())
