import polars as pl
import torch

if torch.cuda.is_available():
    print(torch.cuda.get_device_name(0))
else:
    print("nope")

print("hello")