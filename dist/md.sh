#!/bin/bash
# 创建一个脚本来生成所有文件
for i in {06..30}
do
  touch "${i}.html"
  touch "${i}.md"
done
