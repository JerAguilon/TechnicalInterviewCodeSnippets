#Question: Basic Regex Matcher

Create a basic regex function that returns true if a `string` matches a `pattern`. This particular
regex language only has 2 special characters, `.` and `*`. 

* `.` Matches any individual character, one time. The empty string *does not* match `.`
* `*` Matches any number of characters, *including* the empty string.

Examples:

```
string: 'foobar'
pattern: '*'
output: True, since * matches everything
```

```
string: 'foobar'
pattern: 'fo.bar'
output: True, since . matches the second o and everything else matches.
```

```
string: 'foobar'
pattern: '*ob.z'
output: False
```
