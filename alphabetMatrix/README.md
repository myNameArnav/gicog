# Alphabet Matrix

If you want to add more letters or symbols, follow the steps

1. Add it to the excel `alphabets.xlsx`, color the excel for the letter/symbol you want to add.

> ![image](https://github.com/myNameArnav/gicog/assets/35961071/a977953e-e171-4522-a2ca-2d778e7eb544)

2. (can do manually also) Use the VBA script `macro.vba` (might not work) in the excel, it fills the cells with 1 or 0 depending on the color

3. Run `alphabetMatrix.json`, and select the letter/symbol and copy it

> ![image](https://github.com/myNameArnav/gicog/assets/35961071/f1e8a28b-a868-4dc0-b85f-e08ef0b7efe7)

4. Run `alphabetsToMatrix.py`, and paste it into the input, it will look like this
```
0	0	1	0	0
0	1	1	1	0
1	0	0	0	1
1	0	0	0	1
1	1	1	1	1
1	0	0	0	1
1	0	0	0	1
```
5. The script will automatically paste the result your clipboard

6. Just add another entry in `alphabetMatrix.json`

