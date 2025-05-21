#!/usr/bin/env python3
import os

def read_template():
    """读取05.html作为模板"""
    template_path = "增长思维/05.html"
    with open(template_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_titles():
    """获取所有文章标题"""
    titles = {
        "06": "发现机会：发散与收敛",
        "07": "抓住机会：从0到1的破局点",
        "08": "大机会：知识结构与精神结构",
        "09": "爆品机会：爆品公式与品牌护城河",
        "10": "跨越周期：你的基因，你的机会",
        "11": "选择模式：目标不同，要素不同",
        "12": "设计模式：设计增强回路和调节回路",
        "13": "设计以用户增长为核心的模式",
        "14": "从连接器模式到整合模式",
        "15": "流量模式和产业中台模式",
        "16": "组织：承接机会的能力",
        "17": "建立组织：人际容纳度",
        "18": "权力设计：企业信息流",
        "19": "创新机制：字节跳动的创新飞轮",
        "20": "组织成长的五个阶段",
        "21": "战略支点与战略杠杆",
        "22": "共生：让渡自我，共享资源",
        "23": "结盟：利益相关人地图",
        "24": "踩中风口：闪电式扩张",
        "25": "跨越周期：进化、进化、进化！",
        "26": "增长台阶：从0到10000",
        "27": "用户深度：从流量到共同体",
        "28": "市场广度：从中国到全世界",
        "29": "我们在三浪并发的时代",
        "30": "你的增长底牌，你的人生底色"
    }
    return titles

def create_html_files():
    """创建06-30的HTML文件"""
    template = read_template()
    titles = get_titles()
    
    for num in range(6, 31):
        num_str = f"{num:02d}"
        if num_str in titles:
            # 替换标题
            new_content = template.replace("你的认知地图，你的战场", titles[num_str])
            # 替换编号
            new_content = new_content.replace("05", num_str)
            
            # 写入新文件
            output_path = f"增长思维/{num_str}.html"
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"已创建: {output_path}")

if __name__ == "__main__":
    create_html_files()