# Date Formats

The lab uses the `YYYYMMDD` format for all dates unless a different format is required by an organization or individual external to the LEB, such as publishers.

`YYYY-MM-DD`, `YYYY/MM/DD`, etc. are OK, too, except when the date appears in a folder name or filename.  In this case, `YYYYMMDD` is preferred because some separatoring characters like `/` are used to separate folders from their contents.

## Why use `YYYYMMDD`?

We use `YYYYMMDD` instead of `DDMMYYYY` or `MMDDYYYY` because

- Files starting with a `YYYYMMDD`-formatted date string are ordered correctly when sorted by filename in computer file explorers
- The individual parts of the date are sorted in order from those that vary from the slowest (`YYYY`) to fastest (`DD`)

`YYMMDD`, i.e. dropping the first two digits of the year, is not acceptable because it can be very difficult to differentiate between the different component parts using this format. For example, does the date string `210722` mean July 21, 2022, July 22, 2021?
