
You can use the **regular expression alternation operator `|`** to search for either `"cat"` or `"dog"` like this:

```regex
cat|dog
```

### ✅ Example in different tools/languages:

---

#### 1. **In `grep` (command line):**

```bash
echo "I have a dog and a cat" | grep -E 'cat|dog'
```

> `-E` enables extended regex for `|` to work.

---

#### 2. **In Python:**

```python
import re

text = "I have a dog and a cat"
match = re.search(r'cat|dog', text)

if match:
    print("Found:", match.group())
```

---

#### 3. **In JavaScript:**

```javascript
let text = "I have a dog and a cat";
let regex = /cat|dog/;
let result = text.match(regex);
console.log(result);  // Output: ["dog"]
```

> It will return the **first match** only unless you use the global flag `/cat|dog/g`.

---

### 📌 Notes:

* `cat|dog` means: match either `"cat"` or `"dog"`.
* If you want to match **whole words only**, you can use word boundaries:

  ```regex
  \b(cat|dog)\b
  ```

Let me know what tool or language you're using if you want a specific example.
