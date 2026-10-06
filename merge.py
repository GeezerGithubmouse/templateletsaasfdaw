import urllib.request

# 优选 IP 来源列表
urls = [
    "https://bestcf.pages.dev/xinyitang3/ipv4.txt",
    "https://bestcf.pages.dev/tiancheng/all.txt",
    "https://bestcf.pages.dev/s5gy/mini.txt",
    "https://bestcf.pages.dev/cmliu/all.txt",
    "https://bestcf.pages.dev/uouin/all.txt",
    "https://bestcf.pages.dev/luoli/all.txt",
    "https://bestcf.pages.dev/lzj/all.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/refs/heads/main/BestCF/bestcfv4.txt",
    "https://bestcf.pages.dev/domain/qms/all.txt",
    "https://bestcf.pages.dev/ircf/ipv4.txt",
    "https://bestcf.pages.dev/domain/senflare/all.txt",
    "https://bestcf.pages.dev/nirevil/ipv4.txt",
    "https://bestcf.pages.dev/vvhan/ipv4.txt",
]

all_ips = set()
req_headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            lines = response.read().decode('utf-8', errors='ignore').splitlines()
            for line in lines:
                line = line.strip()
                # 剔除空白、整行注释行以及非 IP 协议行
                if line and not line.startswith('#') and not line.startswith('sub://'):
                    all_ips.add(line)
    except Exception:
        pass

# 排序并截取前 1000 个
sorted_ips = sorted(all_ips)[:1000]

with open("ip.txt", "w", encoding="utf-8") as f:
    for ip in sorted_ips:
        f.write(ip + "\n")
