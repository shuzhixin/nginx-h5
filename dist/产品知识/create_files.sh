#!/bin/bash

# 创建产品知识目录（如果不存在）
#mkdir -p "产品知识"

# 使用循环创建01-30的文件
for i in {1..30}
do
    # 使用printf格式化数字为两位，如01、02等
    filename=$(printf "%02d" $i)
    touch "./${filename}.md"
done

echo "已创建30个md文件在产品知识目录下"