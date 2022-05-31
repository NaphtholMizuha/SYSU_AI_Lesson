# 支持集策略归结推理程序

## 结构

- `main.py` 主程序，使用时请执行该脚本。
- `literal.py` 文字及其相关算法。
- `clause.py` 子句及其算法，包括MCU算法和单步归结算法。
- `clause_set.py` 子句集及其相关算法，包括支持集归结算法。
- `parse.py` 将文本解释为相应数据结构的算法。

## 用法
将子句集录入 `main.py` 同目录下的 `src.txt` 文件夹。
录入格式类似于:
```text
GradStudent(sue)
(¬GradStudent(x), Student(x))
(¬Student(x), HardWorker(x))
¬HardWorker(sue)
```

再执行 `main.py`。

```bash
python3 main.py
```

即可获得推理结果。