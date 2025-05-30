import requests
import schedule
import time
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('site_monitor.log'),
        logging.StreamHandler()
    ]
)

def check_site(url, max_retries=3, timeout=10):
    """
    检查网站是否可访问
    
    Args:
        url: 要监控的网站URL
        max_retries: 最大重试次数
        timeout: 请求超时时间(秒)
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                logging.info(f"网站访问正常 - HTTP状态码: {response.status_code}")
                return True
            else:
                logging.warning(f"网站返回异常状态码: {response.status_code} (尝试 {attempt + 1}/{max_retries})")
        except requests.RequestException as e:
            logging.error(f"访问失败: {str(e)} (尝试 {attempt + 1}/{max_retries})")
            if attempt == max_retries - 1:
                logging.critical(f"网站似乎已经离线 - 已重试{max_retries}次")
                return False
        time.sleep(2)  # 重试前等待2秒
    return False

def monitor_task():
    """定时监控任务"""
    url = "https://nginx-h5-161862-9-1359203558.sh.run.tcloudbase.com/"
    logging.info(f"开始检查网站状态: {url}")
    check_site(url)

def main():
    logging.info("网站监控服务启动")
    
    # 设置定时任务 - 每25分钟执行一次
    schedule.every(25).minutes.do(monitor_task)
    
    # 立即执行一次
    monitor_task()
    
    # 保持程序运行并执行定时任务
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("监控服务已停止")
            break
        except Exception as e:
            logging.error(f"发生未预期的错误: {str(e)}")
            time.sleep(60)  # 发生错误时等待1分钟后继续

if __name__ == "__main__":
    main()