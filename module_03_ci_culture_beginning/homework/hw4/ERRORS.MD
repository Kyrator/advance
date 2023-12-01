## Задача 4. Доверяй, но проверяй
### Что нужно сделать


ошибки 
1. Не импортирован модуль datetime
```python
import datetime
```

2. Не корректное вычисление "return self.yob - now.year"
```python
return now.year - self.yob
```

3. Не корректно прописан присвоение данных пременной "self.name"
```python
def set_name(self, name: str) -> None:
    self.name = self.name
```

4. Не корректно прописан оператор присвоения вместо "==" нужно "="
```python
def set_address(self, address: str) -> None:
    self.address == address
```
