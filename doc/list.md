## List

<p>List the entire representations with their contents privately or non-privately.</p>

**Command**: `cboard list [OPTIONS]`

**Options**

| Option      | Description                        |                 |
| ----------- | ---------------------------------- | --------------- |
| `--help`    | Shows the help menu                | `DEFAULT=False` |
| `--private` | Keeps the contents private/visible | `DEFAULT=True`  |

**Example**

```
$ cboard list --no-private
ghtoken: *** 
googlepw: ****
my_note: **** **** **** ** * ***** ***
```

---

```
$ cboard list --no-private
ghtoken: 123
googlepw: 3215
my_note: Star this repo if I liked it.
```
