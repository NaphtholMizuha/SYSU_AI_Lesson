# 启发式搜索

## 运行方法

在本目录打开终端, 运行:

```shell
python3 main.py
```

如果想更换puzzle, 可以更改`src.txt`的内容.
一些示例存放于`src.txt`中.

运行之后会将运行消耗时间输出到标准输出, 而算法得出的结果
将会输出至`A*_output.txt`和`IDA*_output.txt`中.

## 文件组成

- `main.py` 主程序
- `puzzle.py` puzzle的数据结构以及启发式函数
- `bfs_star.py` A*算法的实现
- `ida_star.py` IDA*算法的实现