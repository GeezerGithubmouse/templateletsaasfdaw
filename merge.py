import urllib.request
import random

# 优选 IP 来源列表（已自动去重）
urls = [
    "https://bestcf.pages.dev/vvhan/ipv4.txt",
    "https://bestcf.pages.dev/nirevil/ipv4.txt",
    "https://bestcf.pages.dev/xinyitang3/ipv4.txt",
    "https://bestcf.pages.dev/kristi/all.txt",
    "https://bestcf.pages.dev/yutian/all.txt",
    "https://bestcf.pages.dev/gslege/Cfxyz.txt",
    "https://bestcf.pages.dev/cmliu/all.txt",
    "https://bestcf.pages.dev/cmliu2/all.txt",
    "https://raw.githubusercontent.com/cmliu/WorkerVless2sub/refs/heads/main/addressesapi.txt",
    "https://bestcf.pages.dev/cfyes/ipv4.txt",
    "https://090227.pages.dev/bestcf?isp=ct&ips=50",
    "https://bestcf.pages.dev/tiancheng/mini.txt",
    "https://bestcf.pages.dev/uouin/all.txt",
    "https://bestcf.pages.dev/luoli/all.txt",
    "https://bestcf.pages.dev/lzj/all.txt",
    "https://bestcf.pages.dev/vps789/top10.txt",
    "https://bestcf.pages.dev/domain/senflare/all.txt",
    "https://bestcf.pages.dev/s5gy/mini.txt",
    "https://bestcf.pages.dev/domain/ircf/all.txt",
    "https://bestcf.pages.dev/zhixuanwang/ipv4-onlyip.txt"
]

all_ips = []
seen = set()
subnet_count = {}  # 用于统计每个 C 段网段保留了多少个 IP

# 伪装浏览器请求头，防止源站防火墙拦截
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

# urls 列表去重，避免重复请求同一个网址
unique_urls = list(dict.fromkeys(urls))

for url in unique_urls:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            lines = response.read().decode('utf-8', errors='ignore').splitlines()
            for line in lines:
                line = line.strip()
                
                # 剔除空白行、整行都是注释的行、订阅协议行以及 HTML 标签
                if not line or line.startswith('#') or line.startswith('sub://') or line.startswith('<'):
                    continue
                
                # 过滤本地无效 IP
                if line.startswith('127.') or line.startswith('0.0.'):
                    continue
                
                if line not in seen:
                    # 提取纯 IP 部分，识别 C 段网段 (如 104.16.1.x)
                    ip_part = line.split(':')[0].split('#')[0].strip()
                    parts = ip_part.split('.')
                    
                    if len(parts) == 4:
                        subnet = f"{parts[0]}.{parts[1]}.{parts[2]}"
                        # 同一个 C 段网段最多保留 3 个 IP，防止堆叠重复无效节点
                        if subnet_count.get(subnet, 0) < 3:
                            subnet_count[subnet] = subnet_count.get(subnet, 0) + 1
                            seen.add(line)
                            all_ips.append(line)
                    else:
                        # 非标准 IPv4 行（如域名或特殊格式）直接保留
                        seen.add(line)
                        all_ips.append(line)
    except Exception:
        pass

# 随机打乱顺序，让各网段和地区分布更均匀
random.shuffle(all_ips)

# 截取网段高度打散后的前 300 个 IP
final_ips = all_ips[:300]

with open("ip.txt", "w", encoding="utf-8") as f:
    for ip in final_ips:
        f.write(ip + "\n")
