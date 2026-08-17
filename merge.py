import urllib.request

# 优选 IP 来源列表
urls = [
    "https://bestcf.pages.dev/domain/mini.txt",
    "https://bestcf.pages.dev/vps789/top10.txt",
    "https://bestcf.pages.dev/domain/qms/all.txt",
    "https://bestcf.pages.dev/domain/senflare/all.txt",
    "https://bestcf.pages.dev/domain/wuya/all.txt",
    "https://bestcf.pages.dev/domain/ircf/all.txt",
    "https://bestcf.pages.dev/wetest/ipv4.txt",
    "https://bestcf.pages.dev/uouin/all.txt",
    "https://bestcf.pages.dev/xinyitang3/ipv4.txt",
    "https://bestcf.pages.dev/luoli/all.txt",
    "https://bestcf.pages.dev/cfyes/ipv4.txt",
    "https://bestcf.pages.dev/tiancheng/mini.txt",
    "https://bestcf.pages.dev/s5gy/mini.txt",
    "https://bestcf.pages.dev/gslege/Cfxyz.txt",
    "https://cf.junzhen.qzz.io/best_ips_bj.txt",
    "https://raw.githubusercontent.com/love-ztm/cfip/refs/heads/main/best_ips.txt",
    "https://bestcf.pages.dev/zhixuanwang/ipv4-onlyip.txt",
    "https://bestcf.pages.dev/vvhan/ipv4.txt",
    "https://bestcf.pages.dev/nirevil/ipv4.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/refs/heads/main/BestCF/bestcfv4.txt",
    "https://raw.githubusercontent.com/yuanxiawan/cfipv4db/refs/heads/main/cfip.txt",
    "https://bestcf.pages.dev/cmliu/all.txt",
    "https://bestcf.pages.dev/cmliu2/all.txt",
    "https://raw.githubusercontent.com/cmliu/WorkerVless2sub/refs/heads/main/addressesapi.txt",
    "https://bestcf.pages.dev/honghong/all.txt",
    "https://bestcf.pages.dev/lzj/all.txt",
    "https://bestcf.pages.dev/lajiao/all.txt",
    "https://bestcf.pages.dev/moistr/all.txt",
    "https://bestcf.pages.dev/kristi/all.txt",
    "https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv4.txt",
    "https://raw.githubusercontent.com/LancelotRar/best-cf-ips/refs/heads/main/best-cf-ipv4.txt",
    "https://raw.githubusercontent.com/Senflare/Senflare-IP/refs/heads/main/Senflare-Pro.txt",
    "https://raw.githubusercontent.com/JieChaoCC/cf-ip-auto/refs/heads/main/data/ipapi.txt",
    "https://raw.githubusercontent.com/ahang39/router/refs/heads/main/all.txt",
    "https://bestcf.pages.dev/ircf/ipv4.txt",
    "https://raw.githubusercontent.com/einsitang/my-fast-cf-ip/refs/heads/master/fastips.txt",
    "https://raw.githubusercontent.com/hubbylei/bestcf/refs/heads/main/bestcf.txt",
    "https://bestcf.pages.dev/yutian/all.txt",
    "https://raw.githubusercontent.com/gshtwy/CF-DNS-Clone/refs/heads/main/wetest-cloudflare-v4.txt",
    "https://bestcf.pages.dev/WARP/WARP-MINI-443.txt",
    "https://090227.pages.dev/bestcf?isp=ct&ips=50",
    "https://randomip.pages.dev/?c=104.16.0.0/12&n=50&p=random"
]

all_ips = set()
req_headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=8) as response:
            lines = response.read().decode('utf-8', errors='ignore').splitlines()
            for line in lines:
                line = line.strip()
                # 剔除空白、注释行以及非 IP 协议行
                if line and not line.startswith('#') and not line.startswith('sub://'):
                    all_ips.add(line)
    except Exception:
        pass

with open("ip.txt", "w", encoding="utf-8") as f:
    for ip in sorted(all_ips):
        f.write(ip + "\n")
