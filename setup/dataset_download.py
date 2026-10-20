import kagglehub

# Download latest version
path = kagglehub.dataset_download("alibekmamyrbay/y-combinator-startups-full-directory-20052026")

print("Path to dataset files:", path)