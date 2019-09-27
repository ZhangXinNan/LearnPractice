

# erase
```c++
	list<int> a = { 0,1,2,3,4,5 };
	list<int>::iterator it = a.begin();
	++it;
	// a = {0,1,2,3,4,5}
	// it -> 1
	list<int>::iterator x = a.erase(it);
	// a = {0,2,3,4,5}
	// it -> {-572662307}
	// x -> 2
```




# insert
```c++
	list<int> a = { 0,1,2,3,4,5 };
	list<int>::iterator it = a.begin();
	++it;
	// a = {0,1,2,3,4,5}
	// it -> 1
	list<int>::iterator y = a.insert(it, 20);
	// a = {0,20, 1,2,3,4,5}
	// it -> 1
	// y -> 20
```
