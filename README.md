# pdf-merge

## Instructions

### If you don't mind the order of the pdf files

Copy ```get_path.sh``` and ```pdf_merge.py``` in with the pdf files you want to merge in a folder.

Run ```pdf_merge.py```

```python3 pdf_merge.py```

### If you mind the orther of the pdf files

Edit ```pdf_merge.py``` and comment the line ```subprocess.call('./get_path.sh')```

Run ```get_path.sh``` in order to create ```paths.txt``` but not merge the files yet.

```sh get_pash.sh```

Edit ```paths.txt``` and place the paths in ascending order from top to bottom 

Run ```pdf_merge.py```

```python3 pdf_merge.py```
