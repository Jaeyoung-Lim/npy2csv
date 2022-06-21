# npy2csv
This repository converts npy files to csv files



```
python3 npy2csv.py <path_to_npy_file> [--output-path=data.csv]

```

An example npy file is in the `resources` folder. To run the example,
```
python3 npy2csv.py resources/test.npy
```

By default the csv file is saved to `./data.csv`. In case you want to change this, you can provide the additional argument `--output-path` to specificy where the csv file should be located.