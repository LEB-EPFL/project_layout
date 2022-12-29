# Filename Guidelines

Naming files and folders is important because good filenames reveal a lot about the data that the files and folders contain. This improves reproducibility because others can more easily understand how different pieces of data came together to produce a paper or presentation.

Below are some guidelines on how to name files and folders.

## Shorter is better, but still try to describe the file

Filenames that are too long are difficult to read and to use in scripts. Instead, try to keep filenames as short as possible, while still including information that helps identify the files' contents.

### Examples

- `hela-trf2-knockdown-a647.tif` **Good**
- `hela-trf2-knockdown-a647-laser-power-200-mw-second-attempt.tif` **Bad: too long**
- `hela.tif` **Bad: too short**

## Characters not to use in filenames

The following characters should not be used anywhere in filenames because these make it harder to use filenames in scripts and may have special meanings for the file system, depending on whether you are using Windows, Mac, or Linux.

- spaces
- slashes (`/` and `\`)
- colons and semicolons (`:` and `;`)

To separate words in a filename, use hyphens (`-`) or underscores (`_`). Do not mix them, however, because it can lead to mistakes.

### Examples

- `hela-trf2-knockdown-a647.tif` **Good**
- `hela_trf2_knockdown_a647.tif` **Good**
- `hela_trf2-knockdown_a647.tif` **Bad: mixes `-` and `_`**
- `hela trf2 knockdown a647.tif` **Bad: uses spaces**

## When a filename or folder name contains a date, put it first

When you put the date first, the file system will naturally sort the files alphabetically.

See [dates.md](dates.md) for how to format the date.

### Examples

- `2022-12-29-hela-trf2-knockdowns` **Good**
- `hela-trf2-knockdowns-2022-12-29` **Bad: date is not first**

## Put the date in the parent folder name when all the files inside come from the same date

You can avoid putting dates in all the filenames of files containing raw data by putting the date in the parent folder. For example, the following folder starts with the date `2022-12-29`.

```console
2022-12-29-trf2-knockdowns/
├── hela-trf2-kd-a647-0.tif
├── hela-trf2-kd-a647-1.tif
└── hela-trf2-kd-a647-2.tif
```

This is better than starting every filename with the date because the resulting filenames are shorter.