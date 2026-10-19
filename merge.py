import urllib.request

# 优选 IP 来源列表
urls = [
    "https://bestcf.pages.dev/domain/mini.txt",
    "https://bestcf.pages.dev/vps789/top10.txt",
    "https://bestcf.pages.dev/domain/ygkkk/all.txt",
    "https://bestcf.pages.dev/domain/qms/all.txt",
    "https://bestcf.pages.dev/domain/senflare/all.txt",
    "https://bestcf.pages.dev/domain/ircf/all.txt",
    "https://bestcf.pages.dev/wetest/ipv4.txt",
    "https://bestcf.pages.dev/uouin/all.txt",
    "https://bestcf.pages.dev/luoli/all.txt",
    "https://bestcf.pages.dev/lzj/all.txt",
    "https://bestcf.pages.dev/xinyitang3/ipv4.txt",
    "https://bestcf.pages.dev/cfyes/ipv4.txt",
    "https://bestcf.pages.dev/tiancheng/mini.txt",
    "https://bestcf.pages.dev/tiancheng/sg.txt",
    "https://bestcf.pages.dev/tiancheng/jp.txt",
    "https://bestcf.pages.dev/tiancheng/hk.txt",
    "https://bestcf.pages.dev/tiancheng/us.txt",
    "https://bestcf.pages.dev/gslege/Cfxyz.txt",
    "https://cf.junzhen.qzz.io/best_ips_bj.txt",
    "https://raw.githubusercontent.com/love-ztm/cfip/refs/heads/main/best_ips.txt",
    "https://bestcf.pages.dev/zhixuanwang/ipv4-onlyip.txt",
    "https://bestcf.pages.dev/s5gy/mini.txt",
    "https://bestcf.pages.dev/s5gy/hk.txt",
    "https://bestcf.pages.dev/s5gy/sg.txt",
    "https://bestcf.pages.dev/s5gy/jp.txt",
    "https://bestcf.pages.dev/s5gy/us.txt",
    "https://bestcf.pages.dev/vvhan/ipv4.txt",
    "https://raw.githubusercontent.com/ymyuuu/IPDB/refs/heads/main/BestCF/bestcfv4.txt",
    "https://raw.githubusercontent.com/yuanxiawan/cfipv4db/refs/heads/main/cfip.txt",
    "https://bestcf.pages.dev/cmliu/all.txt",
    "https://bestcf.pages.dev/cmliu2/all.txt",
    "https://raw.githubusercontent.com/cmliu/WorkerVless2sub/refs/heads/main/addressesapi.txt",
    "https://raw.githubusercontent.com/LancelotRar/best-cf-ips/refs/heads/main/best-cf-ip-scanned-top20.txt",
    "https://raw.githubusercontent.com/joname1/BestCFip/refs/heads/main/ipv4.txt",
    "https://raw.githubusercontent.com/ahang39/router/refs/heads/main/all.txt",
    "https://raw.githubusercontent.com/einsitang/my-fast-cf-ip/refs/heads/master/fastips.txt",
    "https://raw.githubusercontent.com/hubbylei/bestcf/refs/heads/main/bestcf.txt",
    "https://raw.githubusercontent.com/gshtwy/CF-DNS-Clone/refs/heads/main/wetest-cloudflare-v4.txt",
    "https://raw.githubusercontent.com/Senflare/Senflare-IP/refs/heads/main/Senflare-Pro.txt",
    "https://raw.githubusercontent.com/JieChaoCC/cf-ip-auto/refs/heads/main/data/ipapi.txt",
    "https://bestcf.pages.dev/ircf/ipv4.txt",
    "https://bestcf.pages.dev/nirevil/ipv4.txt",
    "https://bestcf.pages.dev/WARP/WARP-MINI.txt",
    "https://090227.pages.dev/bestcf?isp=ct&ips=50",
    "https://randomip.pages.dev/?c=104.16.0.0/12&n=50&p=random",
    "https://bestcf.pages.dev/moistr/all.txt",
    "https://bestcf.pages.dev/kristi/all.txt",
    "https://bestcf.pages.dev/yutian/all.txt",
    "https://raw.githubusercontent.com/Fiatnorm/OptiDomain-Pages/refs/heads/main/optimized_cf_ips.txt",
    "https://bestcf.pages.dev/tiancheng2/mini.txt",
    "https://bestcf.pages.dev/tiancheng3/mini.txt",
]

# 欧洲相关关键词列表（仅匹配带备注或明确标签的行）
EU_KEYWORDS = [
    "欧洲",
    "德国",
    "法国",
    "英国",
    "荷兰",
    "意大利",
    "西班牙",
    "瑞士",
    "瑞典",
    "波兰",
    "俄罗斯",
    "芬兰",
    "比利时",
    "奥地利",
    "GERMANY",
    "FRANCE",
    "UNITED KINGDOM",
    "NETHERLANDS",
    "EUROPE",
    "FRA",
    "MUC",
    "BER",
    "CDG",
    "LHR",
    "AMS",
]


def is_europe(line):
    """仅当存在备注且备注中明确包含欧洲相关地区词汇时，才判定为 True"""
    line_upper = line.upper()

    # 针对带有 # 备注的行进行精准提取与比对
    if "#" in line_upper:
        remark = line_upper.split("#", 1)[1]
        for kw in EU_KEYWORDS:
            if kw in remark:
                return True

    # 针对无 # 但用空格/连字符包含中文地名的行（如 "104.16.1.1 德国"）
    for cn_kw in [
        "欧洲",
        "德国",
        "法国",
        "英国",
        "荷兰",
        "意大利",
        "西班牙",
        "瑞士",
        "瑞典",
        "波兰",
        "俄罗斯",
    ]:
        if cn_kw in line_upper:
            return True

    return False


all_ips = set()
req_headers = {"User-Agent": "Mozilla/5.0"}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            lines = (
                response.read().decode("utf-8", errors="ignore").splitlines()
            )
            for line in lines:
                line = line.strip()
                # 剔除空白、整行注释行以及非 IP 协议行
                if (
                    line
                    and not line.startswith("#")
                    and not line.startswith("sub://")
                ):
                    # 仅在此处过滤掉带欧洲备注的节点
                    if not is_europe(line):
                        all_ips.add(line)
    except Exception:
        pass

# 排序并截取前 1000 个
sorted_ips = sorted(all_ips)[:1000]

with open("ip.txt", "w", encoding="utf-8") as f:
    for ip in sorted_ips:
        f.write(ip + "\n")
